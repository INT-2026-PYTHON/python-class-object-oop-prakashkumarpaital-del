"""
## 4. Counter Class with Class vs Instance Attributes  *(Medium)*

=================================================
COUNTER WITH CLASS VS INSTANCE ATTRIBUTES
=================================================

Problem Statement:
Write a Python CLASS called `Counter` that
maintains:
   - an INSTANCE counter for the current
     object (its own count)
   - a CLASS counter shared across ALL objects
     (the total count across the program)

The goal of this problem is to understand the
difference between:
   - INSTANCE attributes  (one per object,
     stored on `self`)
   - CLASS attributes     (one for the whole
     class, stored on the class itself)

-------------------------------------------------
Instructions:
1. Define the class:
      class Counter:
          total = 0       # CLASS attribute

          def __init__(self, name):
              self.name  = name
              self.count = 0   # INSTANCE attribute
2. Instance methods:
      - increment(self, step=1)
            * self.count  += step
            * Counter.total += step
        (note: use Counter.total, NOT self.total,
         when UPDATING the class attribute)
      - reset(self)
            * sets self.count back to 0
            * does NOT touch Counter.total
      - __str__(self)
            * "<name>: count=<count>"
3. Class method (regular method that touches
   class attribute):
      - show_total() can be a @staticmethod or
        a regular function inside the class
        that returns Counter.total
4. In the driver code:
      - create at least THREE Counter objects
      - call increment() a different number of
        times on each
      - reset ONE of them
      - print each object using print(c)
      - print the overall Counter.total
5. Do NOT use:
   - the global keyword
   - any external library

-------------------------------------------------
Input Example:
c1 = Counter("clicks")
c2 = Counter("views")
c3 = Counter("downloads")

for _ in range(3):
    c1.increment()
for _ in range(5):
    c2.increment()
c3.increment(10)
c1.reset()

Output Example:
clicks:    count=0
views:     count=5
downloads: count=10
Total across all counters: 18

-------------------------------------------------
Explanation:
- `c1.count`, `c2.count`, and `c3.count` are
  three SEPARATE numbers, because each lives
  on its own object.
- `Counter.total` is a SINGLE number shared by
  the whole class. Every increment() call adds
  to it, including the ones that were later
  reset on the instance.
- This is why c1 shows 0 but the class total
  is still 18 (3 + 5 + 10).
=================================================

"""
def get_numeric_input(prompt, default_value=None):
    while True:
        user_input = input(prompt)
        if not user_input and default_value is not None:
            return default_value
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

class Counter:
    total = 0

    def __init__(self, name):
        self.name = name
        self.count = 0

    def increment(self, step=1):
        self.count += step
        Counter.total += step

    def reset(self):
        self.count = 0

    @staticmethod
    def show_total():
        return Counter.total

    def __str__(self):
        return f"{self.name}: count={self.count}"

num_counters = int(get_numeric_input("Enter number of counters to create: "))
counters = []
for i in range(num_counters):
    counter_name = input(f"Enter name for Counter {i+1}: ")
    counters.append(Counter(counter_name))

if counters:
    if len(counters) >= 1:
        increment_c1 = int(get_numeric_input(f"Enter number of increments for {counters[0].name}: "))
        for _ in range(increment_c1):
            counters[0].increment()

    if len(counters) >= 2:
        increment_c2 = int(get_numeric_input(f"Enter number of increments for {counters[1].name}: "))
        for _ in range(increment_c2):
            counters[1].increment()

    if len(counters) >= 3:
        increment_step_c3 = int(get_numeric_input(f"Enter increment step for {counters[2].name}: "))
        counters[2].increment(increment_step_c3)

    if len(counters) >= 1:
        reset_choice = input(f"Do you want to reset {counters[0].name}? (yes/no): ").lower()
        if reset_choice == 'yes':
            counters[0].reset()

    for counter in counters:
        print(counter)
    print(f"Total across all counters: {Counter.show_total()}")
else:
    print("No counters were created.")