# tracker.py
def clean_code(text):
    """Return a tracking code with spaces removed and capitals applied."""
    return text.strip().upper()

def find_parcel(parcels, code):
    """Return the parcel record for a tracking code, or None."""
    for parcel in parcels:
        if parcel["code"] == code:
            return parcel
    return None

def update_status(parcels, code, new_status):
    """Set a parcel's status. Return True if found, False if not."""
    parcel = find_parcel(parcels, code)
    if parcel is None:
        return False
    parcel["status"] = new_status
    return True


