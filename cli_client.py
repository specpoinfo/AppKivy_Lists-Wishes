# encoding: utf-8
import uuid
from argparse import ArgumentParser
import client_api as api


if __name__ == "__main__":
    parser = ArgumentParser()
    sp = parser.add_subparsers(dest="cmd")

    create_sub = sp.add_parser('create', help="Create list")
    create_sub.add_argument('title', help="List title", nargs="?")
    create_sub = sp.add_parser('show', help="Show lists IDs")
    create_sub = sp.add_parser('showlist', help="Show list content")
    create_sub.add_argument('listid', help="List ID")
    create_sub = sp.add_parser('dellist', help="Remove list")
    create_sub.add_argument('listid', help="List ID")
    args = parser.parse_args()
    if args.cmd == "create":
        print(api.createlist(args.title))
    elif args.cmd == "show":
        print(api.getuserlistids())
    elif args.cmd == "showlist":
        print(api.getlistobj(uuid.UUID(args.listid)))
    elif args.cmd == "dellist":
        print(api.dellist(uuid.UUID(args.listid)))
