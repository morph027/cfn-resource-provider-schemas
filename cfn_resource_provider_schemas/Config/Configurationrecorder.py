SCHEMA = {
  "typeName" : "AWS::Config::ConfigurationRecorder",
  "description" : "Resource Type definition for AWS::Config::ConfigurationRecorder",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "RecordingGroup" : {
      "$ref" : "#/definitions/RecordingGroup"
    },
    "RecordingMode" : {
      "$ref" : "#/definitions/RecordingMode"
    },
    "RoleARN" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "RecordingStrategy" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "UseOnly" : {
          "type" : "string"
        }
      },
      "required" : [ "UseOnly" ]
    },
    "ExclusionByResourceTypes" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceTypes" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "ResourceTypes" ]
    },
    "RecordingModeOverride" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ResourceTypes" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "RecordingFrequency" : {
          "type" : "string"
        },
        "Description" : {
          "type" : "string"
        }
      },
      "required" : [ "ResourceTypes", "RecordingFrequency" ]
    },
    "RecordingGroup" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IncludeGlobalResourceTypes" : {
          "type" : "boolean"
        },
        "ResourceTypes" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string"
          }
        },
        "RecordingStrategy" : {
          "$ref" : "#/definitions/RecordingStrategy"
        },
        "ExclusionByResourceTypes" : {
          "$ref" : "#/definitions/ExclusionByResourceTypes"
        },
        "AllSupported" : {
          "type" : "boolean"
        }
      }
    },
    "RecordingMode" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RecordingModeOverrides" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/RecordingModeOverride"
          }
        },
        "RecordingFrequency" : {
          "type" : "string"
        }
      },
      "required" : [ "RecordingFrequency" ]
    }
  },
  "required" : [ "RoleARN" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}