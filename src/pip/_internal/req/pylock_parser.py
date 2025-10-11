import tomllib

def parse_pylock_toml(file_path):
    """
    Parse a pylock.toml file and yield dicts with keys:
    - name
    - version
    - wheel_name
    - wheel_url
    - wheel_hash
    """
    with open(file_path, "rb") as f:
        data = tomllib.load(f)
    results = []
    for pkg in data.get("packages", []):
        pkg_name = pkg.get("name")
        pkg_version = pkg.get("version")
        for wheel in pkg.get("wheels", []):
            wheel_name = wheel.get("name")
            wheel_url = wheel.get("url")
            wheel_hash = wheel.get("hashes", {}).get("sha256")
            results.append({
                "name": pkg_name,
                "version": pkg_version,
                "wheel_name": wheel_name,
                "wheel_url": wheel_url,
                "wheel_hash": wheel_hash,
            })
    return results
