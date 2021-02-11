import argparse
from time_recordeeer import emboss_handler
from time_recordeeer import find_handler
from time_recordeeer import status_handler

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers()

    find_parser = sub_parser.add_parser('find', help='Display specify date attendance data.')
    find_parser.add_argument('date')
    find_parser.add_argument('-f', default='./worktime.csv', help='attendance file path')
    find_parser.set_defaults(func=find_handler.handle)

    emboss_parser = sub_parser.add_parser('emboss', help='Register the stamping information of the specified employee.')
    emboss_parser.add_argument('state', type=str, choices=['clock_in', 'break_begin', 'break_end', 'clock_out'])
    emboss_parser.set_defaults(func=emboss_handler.handle)

    status_parser = sub_parser.add_parser('status', help='fetch to attendance state')
    status_parser.set_defaults(func=status_handler.handle)

    args = parser.parse_args()
    print(args.func(args))
