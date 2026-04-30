from fastapi import Request

#first middleware
async def users_only_middleware(request: Request, call_next):
    if request.url.path.startswith("/users"):
        print("User Middleware: Before processing the request")
        response = await call_next(request)
        print("User Middleware: After processing the request, before returning response")
        return response
    else:
        print(f"User Middleware: Skipping middleware for {request.url.path}")
        response = await call_next(request)
        return response

#second middleware
async def product_only_middleware(request: Request, call_next):
    if request.url.path.startswith("/products"):
        print("Product Middleware: Before processing the request")
        response = await call_next(request)
        print("Product Middleware: After processing the request, before returning response")
        return response
    else:
        print(f"Product Middleware: Skipping middleware for {request.url.path}")
        response = await call_next(request)
        return response