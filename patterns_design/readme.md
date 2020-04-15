
## Interfaces:
### Creational Patterns (Polymorphism) 

- Definition

        Used to create objects in a systematic way
    
- Benefits

        Flexibility
    
        Example: Different subtypes of objects from the same class at runtime
        
### Structural Patterns (Inheritance)

- Definition

        Establishes useful relationships between software components in certain configuration
        To accomplish a goal: both functional and nonfunctional
        Different goals yield different structured      
 

### Behavioral Patterns (Methods and their signatures)
    
- Definition
        
        Best practices of objects interaction
       
- Focus

        Define the protocols
      
 
 ## Object-Oriented Programming OOP
 ### Core concepts
 
 - Objects
    - Represent entities in both problem and solution domains
 - Classes
    - Templates to create objects to avoid recreating them each time
        
            Cookie cutter: replicates objects 
 
 ### Classes define objects in terms of...
- Attributes
    - Represents
        
            Properties of an entity
    - Captures
    
            The state of the entity
            
- Methods
    - Represents
    
            Behaviors
        
  
## Inheritance

- Establishes a relationships between two Classes as **parent and child**
 
#### Child Class
- **Keeps** the Attributes and methods of its parent
- **Adds** new Attributes or methods of its own
- **Overrides** the existing methods of its parent

#### Example
- Pet Class:
    - Dog Class
    - Cat Class
 
## Polymorphism
- Relies on Inheritance
- Allows child classes to be instantiated and treated as the same type as its parent
- Enables a parent class to be manifested into any of its child classes

#### Example
- **User of the Pet class** 
Does not have to know if the pet objects is dor or cat until the runtime
- **True nature of objects**
Hidden until its method is invoked

### A Pattern Context
- **Participants**
    - **Classes involved to form a design pattern**
    - **Roles**
    
- **Quality Attributes**
    - **Nonfunctional requirements**
        
            Usability, modifiability, reliability, performance, etc.
    - **Effect on the entire software**
            
            Architectural solution
- **Forces**
    - **Various factors or trade-offs to consider**
            
            Manifested in quality Attributes

- **Consequences**
    - **Side effects**
            
            Better security but worse performance
            
    - **Decision makers**
        
            Despite the consequences

## Pattern Language
- Name
    - Should capture the gist (суть) of the pattern
    - Becomes part of a vocabulary during the design process
    - Needs to be
        - Meaningful
        - Memorable
- Context
    - Provides a scenario
        - Patterns may be used
    - Provides more insights
        - When to use its
        - When not to use it
- Problem
    - Describes a design challenge
        - Pattern is addressing
- Solution
    - Specifies a pattern
        - Structure: relationships among elements
        - Behavior: interactions
- Related Patterns
    - List of other patterns
        - Used together with the pattern being described 
        - Similar but different
