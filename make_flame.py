# SPDX-FileCopyrightText: 2020 Diego Elio Pettenò
#
# SPDX-License-Identifier: MIT

import argparse
import textwrap

import noise


def flicker_noise(
    step: int, scale: float, octaves: int, lacunarity: float, persistence: float
) -> int:

    # Generate raw perlin noise value, in (-1.0, 1.0) range.
    value = noise.pnoise1(
        step / scale, octaves=octaves, lacunarity=lacunarity, persistence=persistence,
    )

    # Normalize to (0, 1.0)
    value = (value + 1) / 2

    # Normalize to (0, 65536)
    return int(value * 2 ** 16)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", action="store", type=str, required=False,default="waveform.py")
    parser.add_argument("--visualize", action="store_true", default=True,required=False)
    parser.add_argument("--scale", action="store", type=float, default=5.0,required=False)
    parser.add_argument("--octaves", action="store", type=int, required=False,default = 2)
    parser.add_argument("--lacunarity", action="store", type=float, required=False,default=6.0)
    parser.add_argument("--persistence", action="store", type=float, required=False,default=0.75)
    parser.add_argument("--length", action="store", type=float, required=False,default=30000, nargs="?")

    args = parser.parse_args()
    the_args = vars(args)
    series = [
        flicker_noise(i, the_args["scale"], the_args["octaves"], the_args["lacunarity"], the_args["persistence"])
        # flicker_noise(i, args.scale, args.octaves, args.lacunarity, args.persistence)
        for i in range(the_args["length"])
    ]

    with open(the_args["output" ], "wt") as output:
        output.write(
            textwrap.dedent(
                f"""\
            import array

            WAVEFORM = array.array("H",
                {series!r}
            )
            """
            )
        )

    if the_args["visualize"]:
        import matplotlib.pyplot as plt

        plt.plot(series)
        plt.show()


if __name__ == "__main__":
    main()