# Scrap Recycling Facility: "Mini-Profits v0.1"  
*A lean system to turn scrap into cash with minimal upfront cost.*  

---

## **Facility Overview**  
- **Goal**: Process metals/plastics into sellable commodities.  
- **Workflow**:  
  Part 1 (Sort) → Part 2 (Shred) → Part 3 (Separate) → Part 4 (Purify) → Part 5 (Sell)`  
- **Symbol Key**:  
  - `→` (`\u2192`): Next step 
  - `←` (`\u2190`): Prev step  
  - `•` (`\u2022`): Category  
  - `■` (`\u25A0`): Action
 
- json dependencies - materials.json, machine_specs.json, flow.json, legend.json

---
## **Part 0: Intake **
**Rule**:
1. People drop off stuff in an understood condition
2. Srounge what you can to process

## **Part 1: Sort **  
**Rules**:  
1. Sell anything that has **no processing** needed (e.g., bare copper) but note items that have potential value increase with processing.  
2. E-waste and items required for process to sell go to Part 2 for shredding.
3. Items with cost involved to make safe to process are noted.
4. Items with cost bypoduct after processing are noted.

**Flow**
1. Items for direct scrap sale sorted.
2. Items for process are sorted into like items and made safe to process within specs


## **Part 2: Granularize**
**Rules**:
1. Input restrictions must be respected
2. Experimental items are seperate from production runs

**Flow**
1. Like items are shredded and collected into buckets or bins to be passed to the next stage


## **Part 3: Seperate**
**Rules**:
1.  Post seperation buckets are clean for each runs
2.  If shred system produces enough shred clean seperation buckets per shred runs

**Flow**
1.  Run shaker table while port collecting each mass seperate


## **Part 4: Electropurify**
**Rules**:
1. Each mass zone or shaker port seperated is run different
2. Magnet seperate Zone A for ferrous removal

**Flow**
1. In flux

## **Part 5: Sell Shit**
**Rules**:
1. Respect the output and sell it but for what it is not more
2. Disrepecting the output will only degrade the effort
3. Find the best price what you have and reconfirm the market regularly


### **Material Master List**  

    **Metals (Ferrous)
    *Steel (Clean)*
    *Steel (Galvanized)*
    *Cast Iron*
    *Stainless Steel (304)*
    *Stainless Steel (430)*

    **Metals (Non-Ferrous)
    *Aluminum (Cans)*
    *Aluminum (Extrusion)*
    *Aluminum (Sheet)*
    *Copper (Bare Bright)*
    *Copper (Insulated)*
    *Brass (Clean)*
    *Brass (Dirty)*
    *Lead (Batteries)*
    *Lead (Wheel Weights)*
    *Zinc*
    *Magnesium*

    **E-Waste Metals
    *Circuit Boards (Low-Grade)*
    *Circuit Boards (High-Grade)*
    *Hard Drives (Aluminum Platters)*
    *Hard Drives (Magnets)*
    *Power Supplies (Copper Windings)*

    **Plastics
    *PET (Bottles)*
    *HDPE (Jugs)*
    *PVC (Pipes)*
    *ABS (Electronics)*
    *Polycarbonate*
    *Nylon*
    *PP (Polypropylene)*
    *PS (Polystyrene)*

    **Maybe Materials (Needs Research)
    *Coated Wire*
    *Mixed Plastics*
    *Rubber (Clean)*
    *Rubber (Contaminated)*

#### **CATEGORIES**
    *ferrous*
	*non-ferrous*
	*e-waste*
	*plastic*
    *rubber*
	*glass*
	*chemical*
	*composite*

#### **HAZARD_TYPES**
    *None*
	*lead*
	*mercury*
	*flammable*
	*sharp*
    *chemical*
	*toxic*
	*reactive*
	*corrosive*
	*biohazard*

#### **material_property_legend**
      // === CORE PROPERTIES (REQUIRED) === //
      *id = Unique lowercase ID*
	  "id": {"type": "str", "rule": "lowercase, no spaces"}
	  *category = string chosen from defined list in flux*
	  "category": {"type": "str"}
	  
	  // === HAZARD HANDLING === //
      *hazard = simple boolean flag for hazard known*
	  "hazard": {"type": "bool"}
	  *hazard_type = Description of hazard known*
	  "hazard_type": {"type": "str"}
	  *requiresPPE = simple boolean flag for ppe*
      "requiresPPE": {"type": "bool"}

      // === PROCESSING CONTROLS === //
	  *direct_sell = no processing other then group for sale*
      "direct_sell": {"type": "bool", "default": False}
	  *experimental = need to track material through facility to understand output and facility interaction*
	  "experimental": {"type": "bool", "default": False}
	  *partFrom = part stage material received from* 
      "partFrom": {"type": "int", "min": 0, "max": 5}
	  *partTo = part stage material is shipped to*
      "partTo": {"type": "int", "min": 1, "max": 5}
	  *intake_notes = extra notes great for direct sell specs*
      "intake_notes": {"type": "str", "optional": True}  # New field for Part 0
	
    },
    "null_policy": {
      "explicit_null_required": true,
      "allowed_null_fields": ["intake_notes"]
    }
<!-- BEGIN legend.json --> 
``` json (open)

"metadata": {
  "encoding": "UTF-8",
  "last_updated": "2025-07-15",
  "schema_version": "0.1.2",
  "validation_rules": {
    "reference": "LEGEND_RULES",
    "categories": "See CATEGORIES list",
    "hazard_types": "See HAZARD_TYPES"
  }
}

# Constants for validation
CATEGORIES = [
    "ferrous", "e-waste", "plastic", "rubber", "glass", "chemical", "composite", "aluminum", "copper", "brass", "bronze", "non ferrous unknown", "zinc", "tin", "silver", "gold", "platinum"
]

PATHS = [
	"direct_sell", "process", "experimental process"
]

HAZARD_TYPES = [
    None, "lead", "mercury", "flammable", "sharp",
    "chemical", "toxic", "reactive", "corrosive", "biohazard"
]

LEGEND_RULES = {
    "id": {"type": "str", "rule": "lowercase, no spaces"},
    "category": {"type": "str"},
    "hazard": {"type": "bool", "default": False},
	"hazard_type": {"type": "str"},
    "requiresPPE": {"type": "bool", "default": False},
	"input_mass": {"type": "number", "unit": "kg"},
    "paths": {{"type": "str"}
		"direct_sell": {
			"allowed": {"type": "bool", "default": False},
			"reason": {"type": "str"}
		},
		"process": {
			"injection_stage": {"type": "int", "min": 0, "max": 5},
			"output_material": {name or id from outputmaterials.json},
			"output_material_mass": {"type": "number", "unit": "kg"},
			"output_waste": {"type": "array",
				"items": {
				"type": "object",
				"required": ["name", "mass_ratio"],
				"properties": {
				"name": {"type": "string", "pattern": "^[a-z_]+$"},
				"mass_ratio": {"type": "number", "minimum": 0, "maximum": 1},
				"disposition": {
				"type": "string",
				"enum": ["reuse", "recycle", "landfill", "hazardous_waste_facility"]},
				"hazard": {"$ref": "#/definitions/hazard_profile"} 
					}
				},
			"uniqueItemProperties": ["name"]  // Prevents duplicate waste types
			},
	},
    "experimental": {"type": "bool", "default": False},
    "partFrom": {"type": "int", "min": 0, "max": 5},
    "partTo": {"type": "int", "min": 1, "max": 5},
    "intake_notes": {"type": "str", "optional": True} 
}
json (close)```
<!-- END legend.json -->

### **Process Flow Restrictions**

** Each flow will assume no experimental parts and each flow will assume the material was processed by the part being passed**

** Part 0 to Part 1
1. People drop shit off in any form
2. Salvage and scrounge what you can

** Part 1 to Part 2
1. max width 150mm

** Part 2 to Part 3
1. Materials are less than or equal to 60mm

** Part 3 to Part 3
1. Further utilize part 3 while adjusting it's ability to do

** Part 3 to Part 4 with magnet
1. Remove ferrous metals and have sorted specific mass particles to run on step 4
2. The use of magnets understood for heavy mass collected but might be benificial to other mass collected bins

** Part 4 to Part 5
1. With use of system and respected data values from measurement items of outputs develope product understanding and seperation for the best bang for your buck.

**

<!-- BEGIN flow.json -->
```json (open)
{
  "facility_flow": {
    "part_interfaces": {
	  "0→1": {
		"type": "tag and categorize materials within known data structure"
	  },
      "1→2": {
        "type": "physical_dimensions",
        "max_width": 150,
        "unit": "mm"
      },
	  "1→5": {
        "type": "category_sort",
        "output_category": "category",
		"conditions": {
			"direct_sell": true,
			"requires_processing": false
		}        
      },
      "2→3": {
        "type": "granulometry",
        "size_range": [1, 50],
        "unit": "mm"
      },
	  "3→3": {
		"type": "granulometry",
        "size_range": [1, 50],
        "unit": "mm",
		"mass_range": [2.7, 8.9],  // Al to Cu densities,
		"reliability_threshold": 8  // 1-10 scale
	  },
	  "3→4": {
		"type": "granulometry",
        "size_range": [1, 50],
        "unit": "mm",
		"mass_range": [2.7, 8.9],  // Al to Cu densities,
		"reliability_threshold": 8  // 1-10 scale
	  },
	  "4→5": {
	    "type": "output_item"
	  }
    }
  }
}

json (close) ```
<!-- END flow.json -->

<!-- Start materials.json -->
``` json (open)
{
  "materials": [
    {      
	  "id": "steel_clean",
      "category": "ferrous",
      "hazard": false,
      "requiresPPE": false,
      "direct_sell": true,
      "experimental": false,
      "partFrom": 1,
      "partTo": 5,
      "intake_notes": "Accepts clean steel only - no coatings"
    },	
    {
      "id": "aluminum_cans",
      "category": "aluminum",
      "hazard": false,
      "requiresPPE": false,
	  "direct_sell": false,
      "experimental": false,
	  "partFrom": 1,
      "partTo": 2      
    },
    {
      "id": "copper_bb",
      "category": "copper",
      "hazard": false,
      "requiresPPE": false,
	  "direct_sell": true,
	  "experimental": false,
      "partFrom": 1,
      "partTo": 5,
      "intake_notes": "No coating, No solder, No contamination"  
    },
    {
      "id": "copper_insulated",
      "category": "copper",
      "hazard": false,
      "requiresPPE": false,
	  "direct_sell": false,
	  "experimental": true,
      "partFrom": 1,
      "partTo": 2
    }
  ]
}
json (close)``` 
<!-- END materials.json -->

<!-- Start machine_specs.json -->
``` json (open)
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mini-Profits Machine Specifications",
  "definitions": {
    "equipment": {
      "type": "array",
      "items": {"type": "string"},
      "minItems": 1
    },
    "throughput": {
      "type": "string",
      "pattern": "^(\\d+(kg|ton|item)\\/hr|NA)$"
    },
    "dimension_spec": {
      "type": "object",
      "properties": {
        "max_width": {"type": "number", "unit": "mm"},
        "max_weight": {"type": "number", "unit": "kg"},
        "material_hardness": {"enum": ["Mohs <3", "Mohs 3-5", "Mohs >5"]}
      }
    },
    "consumable": {
      "type": "object",
      "patternProperties": {
        "^.*$": {"type": "string", "pattern": "^\\$\\d+(\\.\\d+)?\\/\\d+kg$"}
      }
    }
  },

  "facility": {
    "part_0": {
      "equipment": ["10_sqft_intake_area"],
      "throughput": "NA",
      "input_specs": {
        "max_width": null,
        "material_hardness": null
      },
      "operating_cost": {
        "labor": "$22/hr",
        "consumables": {}
      }
    },
    "part_1": {
      "equipment": ["magnetic_sorter", "manual_sort_table"],
      "throughput": "100kg/hr",
      "input_specs": {
        "max_width": null,
        "material_hardness": null
      },
      "operating_cost": {
        "labor": "$22/hr",
        "consumables": {
          "magnet": "$5/1000kg",
          "chopsaw": "$50/1000kg",
          "sawsall": "$50/1000kg"
        }
      }
    },
    "part_2": {
      "equipment": ["dual_shaft_shredder"],
      "throughput": "80kg/hr",
      "input_specs": {
        "max_width": 150,
        "material_hardness": "Mohs <5"
      },
      "output_specs": {
        "max_width": 5,
        "granulometry": "1-50mm"
      },
      "operating_cost": {
        "labor": "$22/hr",
        "power_unit": "18hp_gas_motor",
        "consumables": {
          "blades": "$120/500kg",
          "gasoline": "$0.30/kg",
          "oil": "$15/liter"
        }
      }
    },
    "part_3": {
      "equipment": ["shaker_table", "water_separator"],
      "throughput": "60kg/hr",
      "input_specs": {
        "max_width": 5,
        "material_hardness": "Mohs <5"
      },
      "output_specs": {
        "mass_groups": 4,
        "moisture_content": "<2%"
      },
      "operating_cost": {
        "labor": "$22/hr",
        "power_units": ["1/2hp_motor", "water_pump"],
        "consumables": {
          "gasoline": "$0.30/kg",
          "oil": "$15/liter"
        }
      }
    },
    "part_4": {
      "equipment": ["electrolysis_tank"],
      "parallel_units": 2,
      "throughput": "40kg/hr",
      "input_specs": {
        "conductivity": ">3.5MS/m"
      },
      "output_specs": {
        "purity": ">98%"
      },
      "operating_cost": {
        "labor": "$28/hr",
        "electricity": "$0.12/kWh",
        "passive_processing": true
      }
    },
    "part_5": {
      "equipment": ["weighing_station", "baling_press"],
      "throughput": "200kg/hr",
      "operating_cost": {
        "labor": "$22/hr"
      }
    }
  }
}
 json (close)```
<!-- END machine_specs.json -->
