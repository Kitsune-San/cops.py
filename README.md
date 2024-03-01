# copspy
copspy is a python API wrapper for the public version of the Critical Ops API.
This project is not affiliated with c-ops, Critical Force, Critical Force Oy or any related company.
This project is purely made for fun by the community and for the community.

# Install:
```bash
  python -m pip install copspy 
```

# Import
```python
  from copspy import get_profile
  from copspy.errors import apierror # For error handling
```

# Ussage examples:
```python
# Get a player profile:
from copspy import get_profile
get_profile.get_player_by_ign("username here")

get_profile.get_player_by_id("id here")

```

# Returns:
When called, the functions will return in json format. Which you can then use for your projects.