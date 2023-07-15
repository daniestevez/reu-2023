#!/usr/bin/env python3

import argparse

import astropy.constants
from astropy.coordinates import SkyCoord, EarthLocation
from astropy.coordinates.name_resolve import NameResolveError
from astropy.time import Time, TimeDelta
import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--carrier-frequency', type=float, required=True,
                        help='Transmit carrier frequency (MHz)')
    parser.add_argument('--observatory', type=str, default='hcro',
                        help=('Observatory name '
                              '[default=%(default)r]'))
    parser.add_argument('--target', type=str, required=True,
                        help='Target name or coordinates')
    parser.add_argument('--start-epoch', type=str, required=True,
                        help='Start epoch (ISO 8601 format)')
    parser.add_argument('--duration', type=float, required=True,
                        help='Duration (seconds)')
    parser.add_argument('--time-step', type=float, default=10.0,
                        help='Time step (seconds) [default=%(default)r]')
    parser.add_argument('--output-file', type=str, required=True,
                        help='Output file path')
    parser.add_argument('--simulation-mode', action='store_true',
                        help='Simulation mode (inverts sign of output)')
    parser.add_argument('--add-offset', type=float, default=0.0,
                        help='Add offset (Hz) to output [default=%(default)r]')
    parser.add_argument('--plot', action='store_true',
                        help='Show plot')
    return parser.parse_args()


def main():
    args = parse_args()

    num_steps = int(np.ceil(args.duration / args.time_step))
    start = Time(args.start_epoch)
    times = (start
             + TimeDelta(args.time_step, format='sec') * np.arange(num_steps))

    try:
        target = SkyCoord(args.target)
    except ValueError as e:
        try:
            target= SkyCoord.from_name(args.target)
        except NameResolveError:
            # re-raise original exception
            raise e

    location = EarthLocation.of_site(args.observatory)
    velocity = -target.radial_velocity_correction(
        kind='heliocentric', obstime=times, location=location).to(u.m/u.s)
    carrier_freq = args.carrier_frequency * 1e6  # convert MHz -> Hz
    doppler = -velocity / astropy.constants.c * carrier_freq

    ts = times.unix
    fs = np.array(doppler.value.data) + args.add_offset
    fs_output = -fs if args.simulation_mode else fs
    with open(args.output_file, 'w') as doppler_file:
        for t, f in zip(ts, fs_output):
            print(t, f, file=doppler_file)

    if args.plot:
        plt.plot(times.datetime, fs)
        plt.title(f'Doppler for {args.target} '
                  f'at {args.carrier_frequency:.3f} MHz '
                  f'(observatory {args.observatory})')
        plt.xlabel('UTC time')
        plt.ylabel('Doppler frequency (Hz)')
        plt.show()


if __name__ == '__main__':
    main()
