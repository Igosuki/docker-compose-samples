import ray
import logging

def main():
    print('Starting Ray head node...')
    ray.init(
        address=None,  # This forces starting a new cluster
        _node_ip_address="0.0.0.0",
        _redis_password=None,
        include_dashboard=True,
        dashboard_host="0.0.0.0",
        dashboard_port=8265,
        ignore_reinit_error=True,
        logging_level=logging.INFO,
        object_store_memory=int(3e9),  # 3GB for object store
        num_cpus=None,  # Use all available CPUs
        _system_config={
            "head_node": True,
            "allow_client_ids": False  # Disable client mode
        }
    )

    print("Ray head node is up and running.")
    print(f"Dashboard URL: http://localhost:8265")
    print(f"Ray head node address: {ray.get_runtime_context().gcs_address}")

if __name__ == "__main__":
    main()
