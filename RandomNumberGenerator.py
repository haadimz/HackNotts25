import random
import os

class ImageSelector:
    def __init__(self, base_path):
        """
        Initialize the image selector with a base path to your image folders.
        
        Args:
            base_path: Root directory containing category folders
        """
        self.base_path = base_path
        
        # Define your main categories
        self.categories = [
            "nature",
            "pets", 
            "hobbies",
            "music_genres",
            "favourite_sport_to_watch",
            "houses",
            "favourite_vacation_spot"
        ]
    
    def generate_random_indices(self):
        """
        Generate random indices (1-3) for all 12 subcategories of a given category.
        
        Args:
            category: The category name (e.g., "houses", "nature")
            
        Returns:
            Dictionary mapping subcategory index to image index
        """
        indices = {}
        for i in range(1, 13):
            # Generate random number between 1 and 3
            image_index = random.randint(1, 3)
            indices[i] = image_index
        
        return indices
    
    def get_image_path(self, category, i, image_index):
        """
        Construct the file path for a specific image.
        
        Args:
            category: Category folder name
            subcategory_num: Subcategory number (1-12)
            image_index: Image index (1-3)
            
        Returns:
            Full path to the image file
        """
        # Adjust this pattern based on your actual folder structure
        # Example: base_path/houses/subcategory_1/image2.jpg
        image_path = os.path.join(
            self.base_path,
            category,
            f"subcategory_{i}",
            f"image{image_index}.jpg"  # Adjust extension as needed
        )
        return image_path
    
    def select_random_images_for_category(self, category):
        """
        Generate random selections and return image paths for all subcategories.
        
        Args:
            category: The category to generate selections for
            
        Returns:
            List of tuples (subcategory_num, image_index, image_path)
        """
        indices = self.generate_random_indices()
        results = []
        
        for i, image_index in indices.items():
            image_path = self.get_image_path(category, i, image_index)
            results.append((i, image_index, image_path))
        
        return results
    
    def run_full_selection(self):
        """
        Run the selection process for ALL categories.
        
        Returns:
            Dictionary with category as key and list of selected images as value
        """
        all_selections = {}
        
        for category in self.categories:
            print(f"\n=== Generating selections for {category} ===")
            selections = self.select_random_images_for_category(category)
            all_selections[category] = selections
            
            # Display the selections
            for i, image_index, image_path in selections:
                print(f"Subcategory {i}: Image {image_index} -> {image_path}")
        
        return all_selections


# Example usage
if __name__ == "__main__":
    # Set your base path - adjust this to your actual directory structure
    BASE_PATH = r"C:\Users\haadi\Documents\GitHub\HackNotts25\topics"  # or use relative path like "./images"
    
    # Create the selector
    selector = ImageSelector(BASE_PATH)
    
    print("\n" + "="*50)
    all_selections = selector.run_full_selection()