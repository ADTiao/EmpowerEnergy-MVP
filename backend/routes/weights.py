from fastapi import APIRouter
from backend.info import info as final
from fastapi.responses import JSONResponse
from fastapi import Request

router = APIRouter()

@router.post("/weights")
async def process_weights(request: Request):
    part = "weights"
    weights = await request.json()
    final[part] = weights


    # OPTIONAL: sanity check
    proposal = final.get("proposal", {})
    missing = []
    for category, metrics in proposal.items():
        for metric in metrics:
            if metric not in weights:
                missing.append(metric)

    if missing:
        print("⚠️ WARNING: Missing weights for:", missing)

    return JSONResponse(content="weights processed", status_code=200)