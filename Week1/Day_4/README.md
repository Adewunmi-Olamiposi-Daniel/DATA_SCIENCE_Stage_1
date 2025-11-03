# DSWK1D4-lists-and-tuples

🗓️ DAY 4 — THURSDAY, OCT 30 – LISTS & TUPLES

WHAT I LEARNED:

Lists are mutable, meaning they can be changed after creation (add, remove, sort, etc.).

Tuples are immutable — once created, they can’t be modified.

Learned to create, slice, and dynamically update lists.

Understood how immutability helps prevent accidental data modification in data pipelines.

MY PRACTICE:

Created an inventory management system that uses both lists and tuples to simulate stock updates and categories.



REFLECTION:

Today reinforced that data structure choice is about intent: when data is expected to change, use lists; when you want to guarantee values remain constant, use tuples. This matters in real-world data work, for example, mutable structures are handy during cleaning and feature engineering, but immutable structures can safely represent metadata, schema definitions, or configuration constants that should not be altered during processing. Being deliberate about this reduces bugs and preserves data integrity in pipelines.
