"""API layer (presentation): FastAPI routers and request/response schemas.

This layer translates HTTP into use-case calls and use-case results back into HTTP.
It holds no business rules.

Rule: code here may import from `application`. It is also the place where concrete
adapters from `infrastructure` are wired to the ports (the composition root).
"""
