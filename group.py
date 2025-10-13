"""
Acquaintance group structure
"""

my_group = [
    {
        "id": 1,  # Unique ID, because name is not unique
        "name": "Jill",
        "age": 26,
        "job": "biologist",
        "connections": [
            {"id": 2, "connection": "friend"},
        ]
    },
    {
        "id": 2,
        "name": "Zalika",
        "age": 28,
        "job": "artist",
        "connections": [
            {"id": 1, "connection": "friend"},
        ]
    },
    {
        "id": 3,
        "name": "John",
        "age": 27,
        "job": "writer",
        "connections": [
            {"id": 2, "connection": "partner"},
        ]
    },
    {
        "id": 4,
        "name": "Nash",
        "age": 34,
        "job": "chef",
        "connections": [
            {"id": 2, "connection": "landlord"},
            {"id": 3, "connection": "cousin"},
        ]
    },
    {
        "id": 5,
        "name": "chenfanghang",
        "age": 25,
        "job": "student",
        "connections": None
    },
]


def get_name_by_id(group_list, param):
    for person in group_list:
        if person.get("id") == param:
            return person.get("name")
    return "Unknown"


def display_group(group_list):
    for person in group_list:
        name = person.get("name")
        age = person.get("age")
        # Handle cases where 'job' is None or not present, for 'no job' consideration
        job = person.get("job") if person.get("job") else "Unemployed"
        connections = person.get("connections", [])

        # 1. Output basic information
        print(f"\n--- {name} (ID: {person['id']}) ---")
        print(f"  Age: {age}")
        print(f"  Job: {job}")

        # 2. Output connections
        if connections:
            print("  Connections:")
            for conn in connections:
                other_name = get_name_by_id(group_list, conn.get("id"))
                rel_type = conn.get("connection")
                print(f"    - Considers {other_name}'s {rel_type}")
        else:
            # Handle no connections
            print("  No connections.")


if __name__ == '__main__':
    display_group(my_group)
