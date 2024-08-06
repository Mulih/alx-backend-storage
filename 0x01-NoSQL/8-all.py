#!/usr/bin/env python3
""" Lists documents. """


def list_all(mongo_collection):
    """ Lists documents in a collection."""
    return [doc for doc in mongo_collection.find()]
