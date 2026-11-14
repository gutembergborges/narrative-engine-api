"""Application layer: use cases and ports.

A use case is one thing the system does ("generate a narrative", "add an item").
A port is an interface (a typing.Protocol) that a use case needs from the outside
world, such as a repository or a narrative generator. This layer defines the ports;
the infrastructure layer implements them.

Rule: code here may import from `domain`, never from `api` or `infrastructure`.

Empty on purpose: the first port and use case are written by hand in Milestone 1.
"""
