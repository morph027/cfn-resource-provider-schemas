SCHEMA = {
  "typeName" : "AWS::IoTWireless::DeviceProfile",
  "description" : "Device Profile's resource schema demonstrating some basic constructs and validation rules.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "LoRaWANDeviceProfile" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SupportsClassB" : {
          "type" : "boolean"
        },
        "ClassBTimeout" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 1000
        },
        "PingSlotPeriod" : {
          "type" : "integer",
          "minimum" : 128,
          "maximum" : 4096
        },
        "PingSlotDr" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 15
        },
        "PingSlotFreq" : {
          "type" : "integer",
          "minimum" : 1000000,
          "maximum" : 16700000
        },
        "SupportsClassC" : {
          "type" : "boolean"
        },
        "ClassCTimeout" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 1000
        },
        "MacVersion" : {
          "type" : "string",
          "maxLength" : 64
        },
        "RegParamsRevision" : {
          "type" : "string",
          "maxLength" : 64
        },
        "RxDelay1" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 15
        },
        "RxDrOffset1" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 7
        },
        "RxFreq2" : {
          "type" : "integer",
          "minimum" : 1000000,
          "maximum" : 16700000
        },
        "RxDataRate2" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 15
        },
        "FactoryPresetFreqsList" : {
          "type" : "array",
          "maxItems" : 20,
          "items" : {
            "$ref" : "#/definitions/FactoryPresetFreq"
          }
        },
        "MaxEirp" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 15
        },
        "MaxDutyCycle" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 100
        },
        "SupportsJoin" : {
          "type" : "boolean"
        },
        "RfRegion" : {
          "type" : "string",
          "maxLength" : 64
        },
        "Supports32BitFCnt" : {
          "type" : "boolean"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    },
    "FactoryPresetFreq" : {
      "type" : "integer",
      "minimum" : 1000000,
      "maximum" : 16700000
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Name of service profile",
      "type" : "string",
      "maxLength" : 256
    },
    "LoRaWAN" : {
      "description" : "LoRaWANDeviceProfile supports all LoRa specific attributes for service profile for CreateDeviceProfile operation",
      "$ref" : "#/definitions/LoRaWANDeviceProfile"
    },
    "Tags" : {
      "description" : "A list of key-value pairs that contain metadata for the device profile.",
      "type" : "array",
      "uniqueItems" : True,
      "maxItems" : 200,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "description" : "Service profile Arn. Returned after successful create.",
      "type" : "string"
    },
    "Id" : {
      "description" : "Service profile Id. Returned after successful create.",
      "type" : "string",
      "maxLength" : 256
    }
  },
  "additionalProperties" : False,
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/LoRaWAN" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotwireless:TagResource", "iotwireless:UntagResource", "iotwireless:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "iotwireless:CreateDeviceProfile", "iotwireless:TagResource" ]
    },
    "update" : {
      "permissions" : [ "iotwireless:GetDeviceProfile", "iotwireless:TagResource", "iotwireless:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "iotwireless:GetDeviceProfile", "iotwireless:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "iotwireless:DeleteDeviceProfile" ]
    },
    "list" : {
      "permissions" : [ "iotwireless:ListDeviceProfiles", "iotwireless:ListTagsForResource" ]
    }
  }
}