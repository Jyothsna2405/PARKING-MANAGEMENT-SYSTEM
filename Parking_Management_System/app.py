from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# ============================================================
# LINKED LIST
# ============================================================

class VehicleNode:

    def __init__(
        self,
        vehicle_id,
        vehicle_number,
        owner_name,
        vehicle_type,
        parking_slot
    ):

        self.vehicle_id = vehicle_id
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type
        self.parking_slot = parking_slot

        self.next = None


class VehicleLinkedList:

    def __init__(self):

        self.head = None

    # ========================================================
    # ADD VEHICLE
    # ========================================================

    def add_vehicle(
        self,
        vehicle_id,
        vehicle_number,
        owner_name,
        vehicle_type,
        parking_slot
    ):

        new_vehicle = VehicleNode(
            vehicle_id,
            vehicle_number,
            owner_name,
            vehicle_type,
            parking_slot
        )

        if self.head is None:

            self.head = new_vehicle

            return

        current = self.head

        while current.next is not None:

            current = current.next

        current.next = new_vehicle

    # ========================================================
    # DISPLAY ALL VEHICLES
    # ========================================================

    def get_all_vehicles(self):

        vehicles = []

        current = self.head

        while current is not None:

            vehicles.append({
                "vehicle_id": current.vehicle_id,
                "vehicle_number": current.vehicle_number,
                "owner_name": current.owner_name,
                "vehicle_type": current.vehicle_type,
                "parking_slot": current.parking_slot
            })

            current = current.next

        return vehicles

    # ========================================================
    # LINEAR SEARCH
    # ========================================================

    def search_vehicle(self, vehicle_number):

        current = self.head

        while current is not None:

            if (
                current.vehicle_number.lower()
                == vehicle_number.lower()
            ):

                return {
                    "vehicle_id": current.vehicle_id,
                    "vehicle_number": current.vehicle_number,
                    "owner_name": current.owner_name,
                    "vehicle_type": current.vehicle_type,
                    "parking_slot": current.parking_slot
                }

            current = current.next

        return None

    # ========================================================
    # FIND VEHICLE NODE
    # ========================================================

    def find_vehicle(self, vehicle_number):

        current = self.head

        while current is not None:

            if (
                current.vehicle_number.lower()
                == vehicle_number.lower()
            ):

                return current

            current = current.next

        return None

    # ========================================================
    # FIND VEHICLE BY ID
    # ========================================================

    def find_vehicle_by_id(self, vehicle_id):

        current = self.head

        while current is not None:

            if str(current.vehicle_id) == str(vehicle_id):

                return current

            current = current.next

        return None

    # ========================================================
    # UPDATE PARKING SLOT
    # ========================================================

    def update_parking_slot(
        self,
        vehicle_number,
        parking_slot
    ):

        current = self.head

        while current is not None:

            if (
                current.vehicle_number.lower()
                == vehicle_number.lower()
            ):

                current.parking_slot = parking_slot

                return True

            current = current.next

        return False


# ============================================================
# CREATE LINKED LIST
# ============================================================

vehicle_list = VehicleLinkedList()


# ============================================================
# BINARY SEARCH TREE - PHASE 2
# ============================================================
#
# BST is organized using Vehicle ID.
#
# Smaller Vehicle ID  -> Left
# Larger Vehicle ID   -> Right
#
# Example:
#
#             105
#            /   \
#          102    108
#         /  \
#       101  103
#
# ============================================================


class BSTNode:

    def __init__(
        self,
        vehicle_id,
        vehicle_number
    ):

        self.vehicle_id = int(vehicle_id)

        self.vehicle_number = vehicle_number

        self.left = None

        self.right = None


class VehicleBST:

    def __init__(self):

        self.root = None

    # ========================================================
    # INSERT
    # ========================================================

    def insert(
        self,
        vehicle_id,
        vehicle_number
    ):

        new_node = BSTNode(
            vehicle_id,
            vehicle_number
        )

        # If tree is empty
        if self.root is None:

            self.root = new_node

            return True

        return self._insert(
            self.root,
            new_node
        )

    # ========================================================
    # INSERT HELPER
    # ========================================================

    def _insert(
        self,
        current,
        new_node
    ):

        # Smaller ID goes to left
        if new_node.vehicle_id < current.vehicle_id:

            if current.left is None:

                current.left = new_node

                return True

            return self._insert(
                current.left,
                new_node
            )

        # Larger ID goes to right
        elif new_node.vehicle_id > current.vehicle_id:

            if current.right is None:

                current.right = new_node

                return True

            return self._insert(
                current.right,
                new_node
            )

        # Duplicate ID
        else:

            return False

    # ========================================================
    # SEARCH
    # ========================================================

    def search(
        self,
        vehicle_id
    ):

        try:

            vehicle_id = int(vehicle_id)

        except ValueError:

            return None

        return self._search(
            self.root,
            vehicle_id
        )

    # ========================================================
    # SEARCH HELPER
    # ========================================================

    def _search(
        self,
        node,
        vehicle_id
    ):

        if node is None:

            return None

        if vehicle_id == node.vehicle_id:

            return {
                "vehicle_id": node.vehicle_id,
                "vehicle_number": node.vehicle_number
            }

        if vehicle_id < node.vehicle_id:

            return self._search(
                node.left,
                vehicle_id
            )

        return self._search(
            node.right,
            vehicle_id
        )

    # ========================================================
    # INORDER TRAVERSAL
    # ========================================================
    #
    # Left -> Root -> Right
    #
    # Gives Vehicle IDs in sorted order.
    #
    # ========================================================

    def inorder(self):

        result = []

        self._inorder(
            self.root,
            result
        )

        return result

    def _inorder(
        self,
        node,
        result
    ):

        if node is not None:

            self._inorder(
                node.left,
                result
            )

            result.append({
                "vehicle_id": node.vehicle_id,
                "vehicle_number": node.vehicle_number
            })

            self._inorder(
                node.right,
                result
            )

    # ========================================================
    # PREORDER TRAVERSAL
    # ========================================================
    #
    # Root -> Left -> Right
    #
    # ========================================================

    def preorder(self):

        result = []

        self._preorder(
            self.root,
            result
        )

        return result

    def _preorder(
        self,
        node,
        result
    ):

        if node is not None:

            result.append({
                "vehicle_id": node.vehicle_id,
                "vehicle_number": node.vehicle_number
            })

            self._preorder(
                node.left,
                result
            )

            self._preorder(
                node.right,
                result
            )

    # ========================================================
    # POSTORDER TRAVERSAL
    # ========================================================
    #
    # Left -> Right -> Root
    #
    # ========================================================

    def postorder(self):

        result = []

        self._postorder(
            self.root,
            result
        )

        return result

    def _postorder(
        self,
        node,
        result
    ):

        if node is not None:

            self._postorder(
                node.left,
                result
            )

            self._postorder(
                node.right,
                result
            )

            result.append({
                "vehicle_id": node.vehicle_id,
                "vehicle_number": node.vehicle_number
            })


# ============================================================
# CREATE BST
# ============================================================

vehicle_bst = VehicleBST()
# ============================================================
# GRAPH - PHASE 3
# BFS + DFS
# ============================================================
#
# The parking area is represented as a graph.
#
# Each parking slot is a NODE.
# The connection between parking slots is an EDGE.
#
# Example:
#
#        P02 -------- P03
#       /  \           |
#     P01  P04 ------- P05
#            \
#             P06
#
# BFS = Breadth First Search
# DFS = Depth First Search
#
# ============================================================


class ParkingGraph:

    def __init__(self):

        # Adjacency list representation
        self.graph = {}


    # ========================================================
    # ADD NODE
    # ========================================================

    def add_node(self, node):

        if node not in self.graph:

            self.graph[node] = []


    # ========================================================
    # ADD EDGE
    # ========================================================

    def add_edge(self, node1, node2):

        # Make sure both nodes exist
        self.add_node(node1)

        self.add_node(node2)

        # Undirected graph
        if node2 not in self.graph[node1]:

            self.graph[node1].append(node2)

        if node1 not in self.graph[node2]:

            self.graph[node2].append(node1)


    # ========================================================
    # BFS - BREADTH FIRST SEARCH
    # ========================================================
    #
    # BFS visits nearby nodes first.
    #
    # It uses a QUEUE.
    #
    # ========================================================

    def bfs(self, start):

        if start not in self.graph:

            return []

        visited = set()

        queue = []

        result = []

        # Start node
        queue.append(start)

        visited.add(start)

        while queue:

            # Remove first element
            current = queue.pop(0)

            result.append(current)

            # Visit connected nodes
            for neighbour in self.graph[current]:

                if neighbour not in visited:

                    visited.add(neighbour)

                    queue.append(neighbour)

        return result


    # ========================================================
    # DFS - DEPTH FIRST SEARCH
    # ========================================================
    #
    # DFS goes deep into one path before
    # coming back.
    #
    # It uses RECURSION / STACK behaviour.
    #
    # ========================================================

    def dfs(self, start):

        if start not in self.graph:

            return []

        visited = set()

        result = []

        self._dfs(
            start,
            visited,
            result
        )

        return result


    # ========================================================
    # DFS HELPER
    # ========================================================

    def _dfs(
        self,
        current,
        visited,
        result
    ):

        visited.add(current)

        result.append(current)

        for neighbour in self.graph[current]:

            if neighbour not in visited:

                self._dfs(
                    neighbour,
                    visited,
                    result
                )


    # ========================================================
    # GET GRAPH
    # ========================================================

    def get_graph(self):

        return self.graph


# ============================================================
# CREATE PARKING GRAPH
# ============================================================

parking_graph = ParkingGraph()


# ============================================================
# ADD PARKING SLOT NODES
# ============================================================

for i in range(1, 11):

    parking_graph.add_node(
        f"P{i:02d}"
    )


# ============================================================
# PARKING SLOT CONNECTIONS
# ============================================================
#
# These connections represent paths between
# different parking slots.
#
# ============================================================

parking_graph.add_edge("P01", "P02")

parking_graph.add_edge("P01", "P04")

parking_graph.add_edge("P02", "P03")

parking_graph.add_edge("P02", "P05")

parking_graph.add_edge("P03", "P06")

parking_graph.add_edge("P04", "P05")

parking_graph.add_edge("P04", "P07")

parking_graph.add_edge("P05", "P06")

parking_graph.add_edge("P05", "P08")

parking_graph.add_edge("P06", "P09")

parking_graph.add_edge("P07", "P08")

parking_graph.add_edge("P08", "P09")

parking_graph.add_edge("P09", "P10")


# ============================================================
# PARKING SLOTS
# ============================================================

parking_slots = []

for i in range(1, 11):

    parking_slots.append({

        "slot_number": f"P{i:02d}",

        "status": "Available",

        "vehicle_number": None
    })


# ============================================================
# QUEUE
# FIFO - FIRST IN, FIRST OUT
# ============================================================

waiting_queue = []


# ------------------------------------------------------------
# ENQUEUE
# ------------------------------------------------------------

def enqueue(vehicle_number):

    waiting_queue.append(vehicle_number)


# ------------------------------------------------------------
# DEQUEUE
# ------------------------------------------------------------

def dequeue():

    if len(waiting_queue) == 0:

        return None

    return waiting_queue.pop(0)


# ------------------------------------------------------------
# GET QUEUE
# ------------------------------------------------------------

def get_queue():

    return waiting_queue.copy()


# ============================================================
# STACK
# LIFO - LAST IN, FIRST OUT
# ============================================================

parking_stack = []


# ------------------------------------------------------------
# PUSH
# ------------------------------------------------------------

def push_operation(operation):

    parking_stack.append(operation)


# ------------------------------------------------------------
# POP
# ------------------------------------------------------------

def pop_operation():

    if len(parking_stack) == 0:

        return None

    return parking_stack.pop()


# ------------------------------------------------------------
# GET STACK
# ------------------------------------------------------------

def get_stack():

    return parking_stack.copy()


# ============================================================
# PAYMENT STATUS
# ============================================================

payment_status = "NOT PAID"


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/dashboard")
def dashboard():

    # Total slots
    total_slots = len(
        parking_slots
    )

    # Count occupied slots
    occupied_slots = 0

    for slot in parking_slots:

        if slot["status"] == "Occupied":

            occupied_slots += 1

    # Available slots
    available_slots = (
        total_slots
        - occupied_slots
    )

    # Waiting vehicles
    waiting_count = len(
        waiting_queue
    )

    # Total vehicle records
    vehicle_count = len(
        vehicle_list.get_all_vehicles()
    )

    # Total BST nodes
    bst_count = len(
        vehicle_bst.inorder()
    )

    return render_template(

        "dashboard.html",

        total_slots=total_slots,

        available_slots=available_slots,

        occupied_slots=occupied_slots,

        waiting_count=waiting_count,

        vehicle_count=vehicle_count,

        bst_count=bst_count
    )


# ============================================================
# VEHICLE MANAGEMENT
# LINKED LIST + BST + PARKING SLOT
# ============================================================

@app.route(
    "/vehicle",
    methods=["GET", "POST"]
)
def vehicle():

    message = None

    message_type = None

    # ========================================================
    # ADD VEHICLE
    # ========================================================

    if request.method == "POST":

        # ----------------------------------------------------
        # GET FORM DATA
        # ----------------------------------------------------

        vehicle_id = request.form.get(
            "vehicle_id",
            ""
        ).strip()

        vehicle_number = request.form.get(
            "vehicle_number",
            ""
        ).strip().upper()

        owner_name = request.form.get(
            "owner_name",
            ""
        ).strip()

        vehicle_type = request.form.get(
            "vehicle_type",
            ""
        ).strip()

        parking_slot_input = request.form.get(
            "parking_slot",
            ""
        ).strip().upper()

        # ----------------------------------------------------
        # BASIC VALIDATION
        # ----------------------------------------------------

        if not vehicle_id:

            message = (
                "Please enter Vehicle ID."
            )

            message_type = "error"

        elif not vehicle_id.isdigit():

            message = (
                "Vehicle ID must contain "
                "numbers only."
            )

            message_type = "error"

        elif not vehicle_number:

            message = (
                "Please enter Vehicle Number."
            )

            message_type = "error"

        elif not owner_name:

            message = (
                "Please enter Owner Name."
            )

            message_type = "error"

        elif not vehicle_type:

            message = (
                "Please select Vehicle Type."
            )

            message_type = "error"

        else:

            # ------------------------------------------------
            # CHECK DUPLICATE VEHICLE ID
            # ------------------------------------------------

            existing_id = (
                vehicle_list.find_vehicle_by_id(
                    vehicle_id
                )
            )

            if existing_id is not None:

                message = (
                    f"Vehicle ID "
                    f"{vehicle_id} "
                    f"already exists."
                )

                message_type = "error"

            else:

                # --------------------------------------------
                # CHECK DUPLICATE VEHICLE NUMBER
                # --------------------------------------------

                existing_vehicle = (
                    vehicle_list.find_vehicle(
                        vehicle_number
                    )
                )

                if existing_vehicle is not None:

                    message = (
                        f"Vehicle "
                        f"{vehicle_number} "
                        f"already exists."
                    )

                    message_type = "error"

                else:

                    # ----------------------------------------
                    # PARKING SLOT
                    # ----------------------------------------

                    selected_slot = None

                    # User entered parking slot
                    if parking_slot_input:

                        # Search requested slot
                        for slot in parking_slots:

                            if (
                                slot["slot_number"].upper()
                                == parking_slot_input
                            ):

                                selected_slot = slot

                                break

                        # ------------------------------------
                        # INVALID SLOT
                        # ------------------------------------

                        if selected_slot is None:

                            message = (
                                f"Parking slot "
                                f"{parking_slot_input} "
                                f"does not exist."
                            )

                            message_type = "error"

                        # ------------------------------------
                        # SLOT OCCUPIED
                        # ------------------------------------

                        elif (
                            selected_slot["status"]
                            == "Occupied"
                        ):

                            message = (
                                f"Parking slot "
                                f"{parking_slot_input} "
                                f"is already occupied "
                                f"by vehicle "
                                f"{selected_slot['vehicle_number']}."
                            )

                            message_type = "error"

                        # ------------------------------------
                        # SLOT AVAILABLE
                        # ------------------------------------

                        else:

                            parking_slot = (
                                selected_slot[
                                    "slot_number"
                                ]
                            )

                            # --------------------------------
                            # ADD TO LINKED LIST
                            # --------------------------------

                            vehicle_list.add_vehicle(

                                vehicle_id,

                                vehicle_number,

                                owner_name,

                                vehicle_type,

                                parking_slot
                            )

                            # --------------------------------
                            # ADD TO BST
                            # --------------------------------

                            vehicle_bst.insert(

                                vehicle_id,

                                vehicle_number
                            )

                            # --------------------------------
                            # OCCUPY PARKING SLOT
                            # --------------------------------

                            selected_slot[
                                "status"
                            ] = "Occupied"

                            selected_slot[
                                "vehicle_number"
                            ] = vehicle_number

                            # --------------------------------
                            # PUSH INTO STACK
                            # --------------------------------

                            push_operation({

                                "vehicle_number":
                                    vehicle_number,

                                "slot_number":
                                    parking_slot
                            })

                            message = (
                                f"Vehicle "
                                f"{vehicle_number} "
                                f"added successfully. "
                                f"Parking slot "
                                f"{parking_slot} "
                                f"is now occupied "
                                f"and the vehicle "
                                f"was inserted into "
                                f"the BST."
                            )

                            message_type = (
                                "success"
                            )

                    # ----------------------------------------
                    # NO PARKING SLOT ENTERED
                    # ----------------------------------------

                    else:

                        parking_slot = (
                            "Not Assigned"
                        )

                        # --------------------------------
                        # ADD TO LINKED LIST
                        # --------------------------------

                        vehicle_list.add_vehicle(

                            vehicle_id,

                            vehicle_number,

                            owner_name,

                            vehicle_type,

                            parking_slot
                        )

                        # --------------------------------
                        # ADD TO BST
                        # --------------------------------

                        vehicle_bst.insert(

                            vehicle_id,

                            vehicle_number
                        )

                        message = (
                            f"Vehicle "
                            f"{vehicle_number} "
                            f"added successfully "
                            f"to the Linked List "
                            f"and BST."
                        )

                        message_type = (
                            "success"
                        )

    # ========================================================
    # DISPLAY VEHICLES
    # ========================================================

    vehicles = (
        vehicle_list.get_all_vehicles()
    )

    return render_template(

        "vehicle.html",

        vehicles=vehicles,

        message=message,

        message_type=message_type
    )


# ============================================================
# BINARY SEARCH TREE PAGE
# PHASE 2
# ============================================================

@app.route(
    "/bst",
    methods=["GET", "POST"]
)
def bst_page():

    search_result = None

    search_message = None

    search_message_type = None

    # ========================================================
    # BST SEARCH
    # ========================================================

    if request.method == "POST":

        action = request.form.get(
            "action"
        )

        if action == "search":

            vehicle_id = request.form.get(
                "vehicle_id",
                ""
            ).strip()

            if not vehicle_id:

                search_message = (
                    "Please enter a Vehicle ID."
                )

                search_message_type = (
                    "error"
                )

            elif not vehicle_id.isdigit():

                search_message = (
                    "Vehicle ID must contain "
                    "numbers only."
                )

                search_message_type = (
                    "error"
                )

            else:

                search_result = (
                    vehicle_bst.search(
                        vehicle_id
                    )
                )

                if search_result is not None:

                    search_message = (
                        f"Vehicle ID "
                        f"{vehicle_id} "
                        f"found in the BST."
                    )

                    search_message_type = (
                        "success"
                    )

                else:

                    search_message = (
                        f"Vehicle ID "
                        f"{vehicle_id} "
                        f"was not found "
                        f"in the BST."
                    )

                    search_message_type = (
                        "error"
                    )

    # ========================================================
    # GET TRAVERSALS
    # ========================================================

    inorder = (
        vehicle_bst.inorder()
    )

    preorder = (
        vehicle_bst.preorder()
    )

    postorder = (
        vehicle_bst.postorder()
    )

    return render_template(

        "bst.html",

        inorder=inorder,

        preorder=preorder,

        postorder=postorder,

        search_result=search_result,

        search_message=search_message,

        search_message_type=search_message_type
    )


# ============================================================
# PARKING SLOT MANAGEMENT
# GREEDY ALGORITHM + STACK
# ============================================================

@app.route(
    "/parking-slots",
    methods=["GET", "POST"]
)
def parking_slots_page():

    message = None

    message_type = None

    if request.method == "POST":

        action = request.form.get(
            "action"
        )

        # ====================================================
        # PARK VEHICLE
        # ====================================================

        if action == "park":

            vehicle_number = request.form.get(
                "vehicle_number",
                ""
            ).strip().upper()

            if not vehicle_number:

                message = (
                    "Please enter a vehicle number."
                )

                message_type = "error"

            else:

                already_parked = False

                # --------------------------------------------
                # CHECK IF VEHICLE IS ALREADY PARKED
                # --------------------------------------------

                for slot in parking_slots:

                    if (
                        slot["vehicle_number"]
                        is not None
                        and
                        slot["vehicle_number"].upper()
                        == vehicle_number
                    ):

                        already_parked = True

                        message = (
                            f"Vehicle "
                            f"{vehicle_number} "
                            f"is already parked "
                            f"in "
                            f"{slot['slot_number']}."
                        )

                        message_type = "error"

                        break

                # --------------------------------------------
                # GREEDY ALGORITHM
                # FIRST AVAILABLE SLOT
                # --------------------------------------------

                if not already_parked:

                    allocated = False

                    for slot in parking_slots:

                        if (
                            slot["status"]
                            == "Available"
                        ):

                            # Occupy slot
                            slot["status"] = (
                                "Occupied"
                            )

                            slot[
                                "vehicle_number"
                            ] = vehicle_number

                            # --------------------------------
                            # UPDATE LINKED LIST
                            # --------------------------------

                            vehicle_node = (
                                vehicle_list.find_vehicle(
                                    vehicle_number
                                )
                            )

                            if vehicle_node is not None:

                                vehicle_node.parking_slot = (
                                    slot["slot_number"]
                                )

                            # --------------------------------
                            # STACK
                            # --------------------------------

                            push_operation({

                                "vehicle_number":
                                    vehicle_number,

                                "slot_number":
                                    slot["slot_number"]
                            })

                            message = (
                                f"Vehicle "
                                f"{vehicle_number} "
                                f"allocated to "
                                f"{slot['slot_number']}."
                            )

                            message_type = (
                                "success"
                            )

                            allocated = True

                            break

                    # ----------------------------------------
                    # NO SLOT AVAILABLE
                    # ----------------------------------------

                    if not allocated:

                        message = (
                            "No parking slots available."
                        )

                        message_type = "error"

        # ====================================================
        # RELEASE PARKING SLOT
        # ====================================================

        elif action == "release":

            slot_number = request.form.get(
                "slot_number",
                ""
            ).strip().upper()

            found = False

            for slot in parking_slots:

                if (
                    slot["slot_number"]
                    == slot_number
                ):

                    found = True

                    vehicle_number = (
                        slot["vehicle_number"]
                    )

                    # Make slot available
                    slot["status"] = (
                        "Available"
                    )

                    slot["vehicle_number"] = None

                    # ----------------------------------------
                    # UPDATE LINKED LIST
                    # ----------------------------------------

                    if vehicle_number is not None:

                        vehicle_list.update_parking_slot(

                            vehicle_number,

                            "Not Assigned"
                        )

                    message = (
                        f"Slot "
                        f"{slot_number} "
                        f"released successfully."
                    )

                    message_type = (
                        "success"
                    )

                    break

            if not found:

                message = (
                    f"Parking slot "
                    f"{slot_number} "
                    f"was not found."
                )

                message_type = "error"

    return render_template(

        "parking-slots.html",

        slots=parking_slots,

        message=message,

        message_type=message_type,

        stack=get_stack()
    )


# ============================================================
# UNDO LAST PARKING OPERATION
# STACK
# LIFO
# ============================================================

@app.route(
    "/undo-parking",
    methods=["POST"]
)
def undo_parking():

    # Get most recent operation
    operation = pop_operation()

    # Stack empty
    if operation is None:

        return redirect(
            "/parking-slots"
        )

    vehicle_number = operation[
        "vehicle_number"
    ]

    slot_number = operation[
        "slot_number"
    ]

    # --------------------------------------------------------
    # RELEASE SLOT
    # --------------------------------------------------------

    for slot in parking_slots:

        if (
            slot["slot_number"]
            == slot_number
        ):

            slot["status"] = (
                "Available"
            )

            slot["vehicle_number"] = None

            break

    # --------------------------------------------------------
    # UPDATE LINKED LIST
    # --------------------------------------------------------

    vehicle_list.update_parking_slot(

        vehicle_number,

        "Not Assigned"
    )

    return redirect(
        "/parking-slots"
    )


# ============================================================
# SEARCH VEHICLE
# LINEAR SEARCH
# ============================================================

@app.route(
    "/search-vehicle",
    methods=["GET", "POST"]
)
def search_vehicle():

    vehicle = None

    message = None

    if request.method == "POST":

        vehicle_number = request.form.get(
            "vehicle_number",
            ""
        ).strip().upper()

        vehicle = (
            vehicle_list.search_vehicle(
                vehicle_number
            )
        )

        if vehicle is None:

            message = (
                f"Vehicle "
                f"{vehicle_number} "
                f"was not found."
            )

    return render_template(

        "search-vehicle.html",

        vehicle=vehicle,

        message=message
    )


# ============================================================
# BUBBLE SORT
# ============================================================

def bubble_sort(vehicles):

    arr = vehicles.copy()

    n = len(arr)

    for i in range(n):

        for j in range(
            0,
            n - i - 1
        ):

            if int(
                arr[j]["vehicle_id"]
            ) > int(
                arr[j + 1]["vehicle_id"]
            ):

                arr[j], arr[j + 1] = (

                    arr[j + 1],

                    arr[j]
                )

    return arr


# ============================================================
# MERGE SORT
# ============================================================

def merge_sort(vehicles):

    if len(vehicles) <= 1:

        return vehicles.copy()

    mid = len(vehicles) // 2

    left = merge_sort(
        vehicles[:mid]
    )

    right = merge_sort(
        vehicles[mid:]
    )

    return merge(
        left,
        right
    )


# ============================================================
# MERGE
# ============================================================

def merge(left, right):

    result = []

    i = 0

    j = 0

    while (
        i < len(left)
        and
        j < len(right)
    ):

        if int(
            left[i]["vehicle_id"]
        ) <= int(
            right[j]["vehicle_id"]
        ):

            result.append(
                left[i]
            )

            i += 1

        else:

            result.append(
                right[j]
            )

            j += 1

    while i < len(left):

        result.append(
            left[i]
        )

        i += 1

    while j < len(right):

        result.append(
            right[j]
        )

        j += 1

    return result


# ============================================================
# SORT RECORDS
# ============================================================

@app.route(
    "/sort-records",
    methods=["GET", "POST"]
)
def sort_records():

    sorted_vehicles = None

    algorithm_name = None

    if request.method == "POST":

        algorithm = request.form.get(
            "algorithm"
        )

        vehicles = (
            vehicle_list.get_all_vehicles()
        )

        # ----------------------------------------------------
        # BUBBLE SORT
        # ----------------------------------------------------

        if algorithm == "bubble":

            sorted_vehicles = (
                bubble_sort(
                    vehicles
                )
            )

            algorithm_name = (
                "Bubble Sort"
            )

        # ----------------------------------------------------
        # MERGE SORT
        # ----------------------------------------------------

        elif algorithm == "merge":

            sorted_vehicles = (
                merge_sort(
                    vehicles
                )
            )

            algorithm_name = (
                "Merge Sort"
            )

    return render_template(

        "sort-records.html",

        sorted_vehicles=sorted_vehicles,

        algorithm_name=algorithm_name
    )


# ============================================================
# WAITING VEHICLES
# QUEUE
# FIFO
# ============================================================

@app.route(
    "/waiting-vehicles",
    methods=["GET", "POST"]
)
def waiting_vehicles():

    message = None

    message_type = None

    if request.method == "POST":

        action = request.form.get(
            "action"
        )

        # ====================================================
        # ENQUEUE
        # ====================================================

        if action == "enqueue":

            vehicle_number = request.form.get(
                "vehicle_number",
                ""
            ).strip().upper()

            if not vehicle_number:

                message = (
                    "Please enter a vehicle number."
                )

                message_type = "error"

            elif (
                vehicle_number
                in waiting_queue
            ):

                message = (
                    f"Vehicle "
                    f"{vehicle_number} "
                    f"is already in the "
                    f"waiting queue."
                )

                message_type = "error"

            else:

                enqueue(
                    vehicle_number
                )

                message = (
                    f"Vehicle "
                    f"{vehicle_number} "
                    f"has joined the "
                    f"waiting queue."
                )

                message_type = "success"

        # ====================================================
        # DEQUEUE
        # ====================================================

        elif action == "dequeue":

            vehicle_number = (
                dequeue()
            )

            if vehicle_number is None:

                message = (
                    "The waiting queue "
                    "is empty."
                )

                message_type = "error"

            else:

                message = (
                    f"Vehicle "
                    f"{vehicle_number} "
                    f"has been processed "
                    f"from the queue."
                )

                message_type = "success"

    return render_template(

        "waiting-vehicles.html",

        queue=get_queue(),

        message=message,

        message_type=message_type
    )


# ============================================================
# PARKING FEES AND PAYMENT
# ============================================================

@app.route(
    "/parking-fees",
    methods=["GET", "POST"]
)
def parking_fees():

    global payment_status

    fee = None

    vehicle_number = None

    hours = None

    payment_done = False

    message = None

    if request.method == "POST":

        action = request.form.get(
            "action"
        )

        # ====================================================
        # CALCULATE FEE
        # ====================================================

        if action == "calculate":

            vehicle_number = request.form.get(
                "vehicle_number",
                ""
            ).strip().upper()

            hours_value = request.form.get(
                "hours",
                ""
            ).strip()

            if not hours_value:

                message = (
                    "Please enter the "
                    "parking duration."
                )

                payment_status = (
                    "NOT PAID"
                )

            else:

                try:

                    hours = int(
                        hours_value
                    )

                    if hours <= 0:

                        raise ValueError

                    rate_per_hour = 20

                    fee = (
                        hours
                        *
                        rate_per_hour
                    )

                    payment_status = (
                        "NOT PAID"
                    )

                    payment_done = False

                except ValueError:

                    message = (
                        "Please enter a "
                        "valid number of hours."
                    )

                    payment_status = (
                        "NOT PAID"
                    )

        # ====================================================
        # PAYMENT
        # ====================================================

        elif action == "pay":

            vehicle_number = request.form.get(
                "vehicle_number",
                ""
            ).strip().upper()

            hours_value = request.form.get(
                "hours",
                ""
            ).strip()

            if not hours_value:

                message = (
                    "Payment failed. "
                    "Parking duration "
                    "is missing."
                )

                payment_status = (
                    "NOT PAID"
                )

            else:

                try:

                    hours = int(
                        hours_value
                    )

                    if hours <= 0:

                        raise ValueError

                    rate_per_hour = 20

                    fee = (
                        hours
                        *
                        rate_per_hour
                    )

                    payment_status = (
                        "PAID"
                    )

                    payment_done = True

                    message = (
                        f"Payment of "
                        f"₹{fee} "
                        f"completed "
                        f"successfully "
                        f"for vehicle "
                        f"{vehicle_number}."
                    )

                except ValueError:

                    message = (
                        "Payment failed. "
                        "Please enter a "
                        "valid duration."
                    )

                    payment_status = (
                        "NOT PAID"
                    )

    return render_template(

        "parking-fees.html",

        fee=fee,

        vehicle_number=vehicle_number,

        hours=hours,

        payment_status=payment_status,

        payment_done=payment_done,

        message=message
    )
# ============================================================
# PARKING GRAPH PAGE
# PHASE 3 - BFS + DFS
# ============================================================

@app.route(
    "/graph",
    methods=["GET", "POST"]
)
def graph_page():

    start_node = "P01"

    bfs_result = []

    dfs_result = []

    message = None

    # ========================================================
    # PROCESS GRAPH SEARCH
    # ========================================================

    if request.method == "POST":

        start_node = request.form.get(
            "start_node",
            "P01"
        ).strip().upper()

        if start_node not in parking_graph.graph:

            message = (
                f"Parking slot "
                f"{start_node} "
                f"does not exist."
            )

        else:

            bfs_result = parking_graph.bfs(
                start_node
            )

            dfs_result = parking_graph.dfs(
                start_node
            )

    else:

        # Default results
        bfs_result = parking_graph.bfs(
            start_node
        )

        dfs_result = parking_graph.dfs(
            start_node
        )

    # ========================================================
    # GRAPH INFORMATION
    # ========================================================

    graph_data = (
        parking_graph.get_graph()
    )

    node_count = len(
        graph_data
    )

    edge_count = sum(
        len(neighbours)
        for neighbours in graph_data.values()
    ) // 2

    return render_template(

        "graph.html",

        graph_data=graph_data,

        bfs_result=bfs_result,

        dfs_result=dfs_result,

        start_node=start_node,

        node_count=node_count,

        edge_count=edge_count,

        message=message
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )