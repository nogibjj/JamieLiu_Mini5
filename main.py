"""Handles CLI commands for the drinks dataset."""

import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    update_record,
    delete_record,
    create_record,
    general_query,
    read_data,
)


def handle_arguments(args):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="ETL-Query script for drinks dataset")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_record",
            "delete_record",
            "create_record",
            "general_query",
            "read_data",
        ],
    )
    args = parser.parse_args(args[:1])

    if args.action == "update_record":
        parser.add_argument("country")
        parser.add_argument("beer_servings", type=int)
        parser.add_argument("spirit_servings", type=int)
        parser.add_argument("wine_servings", type=int)
        parser.add_argument("total_alcohol", type=float)

    if args.action == "create_record":
        parser.add_argument("country")
        parser.add_argument("beer_servings", type=int)
        parser.add_argument("spirit_servings", type=int)
        parser.add_argument("wine_servings", type=int)
        parser.add_argument("total_alcohol", type=float)

    if args.action == "general_query":
        parser.add_argument("query")

    if args.action == "delete_record":
        parser.add_argument("country")

    # Parse again with specific args
    return parser.parse_args(sys.argv[1:])


def main():
    """Handles all CLI commands for the drinks dataset."""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "update_record":
        update_record(
            args.country,
            args.beer_servings,
            args.spirit_servings,
            args.wine_servings,
            args.total_alcohol,
        )
    elif args.action == "delete_record":
        delete_record(args.country)
    elif args.action == "create_record":
        create_record(
            args.country,
            args.beer_servings,
            args.spirit_servings,
            args.wine_servings,
            args.total_alcohol,
        )
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_data":
        data = read_data()
        print(data)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
