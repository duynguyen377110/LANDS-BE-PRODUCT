config_queue = {

    "CATEGORY": {
        "NEW": {
            "CONSUMER": "NEW-CATEGORY",
            "REFLY": "REFLY-NEW-CATEGORY"
        },
        "UPDATE": {
            "CONSUMER": "UPDATE-CATEGORY",
            "REFLY": "REFLY-UPDATE-CATEGORY"
        },
        "DELETE": {
            "CONSUMER": "DELETE-CATEGORY",
            "REFLY": "REFLY-DELETE-CATEGORY"
        }
    },
    "PRODUCT":{
        "NEW": {
            "CONSUMER": "NEW-PRODUCT",
            "REFLY": "REFLY-NEW-PRODUCT"
        },
        "DELETE": {
            "CONSUMER": "DELETE-PRODUCT",
            "REFLY": "REFLY-DELETE-PRODUCT"
        }
    }
}