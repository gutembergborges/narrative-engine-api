"""Infrastructure layer: adapters that talk to the outside world.

PostgreSQL repositories, the Redis cache and LLM provider clients live here. Each
adapter implements a port defined in the application layer, so it can be swapped
(for example, a fake LLM in tests) without touching use cases or the domain.

Rule: code here may import from `application` and `domain`, never from `api`.

Empty on purpose: the first adapter is written by hand in Milestone 1.
"""
