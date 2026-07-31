# """
# Defines the required fields for each supported intent.

# The orchestrator uses this mapping to determine
# what information is still needed before executing a tool.
# """

# REQUIRED_FIELDS = {
#     # -------------------------
#     # Pet Operations
#     # -------------------------
#     "create_pet": [
#         "petname",
#         "species",
#         "breed",
#         "age",
#         "owner",
#     ],

#     "update_pet": [
#         "pet",
#     ],

#     "delete_pet": [
#         "pet",
#     ],

#     "get_pet": [
#         "pet",
#     ],

#     "get_all_pets": [],

#     # -------------------------
#     # Owner Operations
#     # -------------------------
#     "create_owner": [
#         "name",
#         "phone",
#         "email",
#     ],

#     "get_owner_pets": [
#         "owner",
#     ],

#     # -------------------------
#     # Visit Operations
#     # -------------------------
#     "create_visit": [
#         "pet",
#         "visit_date",
#         "reason",
#         "diagnosis",
#         "treatment",
#     ],

#     "update_visit": [
#         "visit",
#     ],

#     "delete_visit": [
#         "visit",
#     ],

#     "get_pet_visits": [
#         "pet",
#     ],
# }