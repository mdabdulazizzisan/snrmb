class ImageProcessor:
    def __init__(self):
        # Directory configurations
        self.original_dir = "original_images"
        self.processed_dir = "processed_images"
        self.links_file = "image_links.txt"
        self.state_file = "processing_state.json"
        
        # Initialize or load state
        self.state = self.load_state()
    
    def load_state(self):
        """Load or create initial state"""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {
            "current_line": 0,
            "current_object": 1,
            "current_image": 1,
            "last_processed_time": None
        }
    
    def save_state(self):
        """Save current state to JSON file"""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=4)
