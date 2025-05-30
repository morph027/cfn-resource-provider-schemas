SCHEMA = {
  "typeName" : "AWS::SSM::MaintenanceWindowTarget",
  "description" : "Resource Type definition for AWS::SSM::MaintenanceWindowTarget",
  "additionalProperties" : False,
  "properties" : {
    "OwnerInformation" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "WindowId" : {
      "type" : "string"
    },
    "ResourceType" : {
      "type" : "string"
    },
    "Targets" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Targets"
      }
    },
    "Id" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "Targets" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Values" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Values", "Key" ]
    }
  },
  "required" : [ "WindowId", "ResourceType", "Targets" ],
  "createOnlyProperties" : [ "/properties/WindowId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}