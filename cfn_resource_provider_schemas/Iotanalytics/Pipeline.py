SCHEMA = {
  "typeName" : "AWS::IoTAnalytics::Pipeline",
  "description" : "Resource Type definition for AWS::IoTAnalytics::Pipeline",
  "additionalProperties" : False,
  "taggable" : True,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "PipelineName" : {
      "type" : "string",
      "pattern" : "[a-zA-Z0-9_]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "PipelineActivities" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "minItems" : 1,
      "maxItems" : 25,
      "items" : {
        "$ref" : "#/definitions/Activity"
      }
    }
  },
  "definitions" : {
    "Activity" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SelectAttributes" : {
          "$ref" : "#/definitions/SelectAttributes"
        },
        "Datastore" : {
          "$ref" : "#/definitions/Datastore"
        },
        "Filter" : {
          "$ref" : "#/definitions/Filter"
        },
        "AddAttributes" : {
          "$ref" : "#/definitions/AddAttributes"
        },
        "Channel" : {
          "$ref" : "#/definitions/Channel"
        },
        "DeviceShadowEnrich" : {
          "$ref" : "#/definitions/DeviceShadowEnrich"
        },
        "Math" : {
          "$ref" : "#/definitions/Math"
        },
        "Lambda" : {
          "$ref" : "#/definitions/Lambda"
        },
        "DeviceRegistryEnrich" : {
          "$ref" : "#/definitions/DeviceRegistryEnrich"
        },
        "RemoveAttributes" : {
          "$ref" : "#/definitions/RemoveAttributes"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
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
      "required" : [ "Value", "Key" ]
    },
    "DeviceShadowEnrich" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Attribute" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "ThingName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "RoleArn" : {
          "type" : "string",
          "minLength" : 20,
          "maxLength" : 2048
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Attribute", "ThingName", "RoleArn", "Name" ]
    },
    "Filter" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Filter" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Filter", "Name" ]
    },
    "RemoveAttributes" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Attributes" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 50,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 256
          }
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Attributes", "Name" ]
    },
    "Datastore" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DatastoreName" : {
          "type" : "string",
          "pattern" : "[a-zA-Z0-9_]+",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "DatastoreName", "Name" ]
    },
    "Channel" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ChannelName" : {
          "type" : "string",
          "pattern" : "[a-zA-Z0-9_]+",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "ChannelName", "Name" ]
    },
    "SelectAttributes" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Attributes" : {
          "type" : "array",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "minItems" : 1,
          "maxItems" : 50,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 256
          }
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Name", "Attributes" ]
    },
    "Lambda" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "BatchSize" : {
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 1000
        },
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "LambdaName" : {
          "type" : "string",
          "pattern" : "[a-zA-Z0-9_-]+",
          "minLength" : 1,
          "maxLength" : 64
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "LambdaName", "Name", "BatchSize" ]
    },
    "DeviceRegistryEnrich" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Attribute" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "ThingName" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "RoleArn" : {
          "type" : "string",
          "minLength" : 20,
          "maxLength" : 2048
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Attribute", "ThingName", "RoleArn", "Name" ]
    },
    "AddAttributes" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Attributes" : {
          "type" : "object",
          "minProperties" : 1,
          "maxProperties" : 50,
          "patternProperties" : {
            "^.*$" : {
              "type" : "string",
              "minLength" : 1,
              "maxLength" : 256
            }
          },
          "additionalProperties" : False
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Attributes", "Name" ]
    },
    "Math" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Attribute" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Next" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Math" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Name" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        }
      },
      "required" : [ "Attribute", "Math", "Name" ]
    }
  },
  "required" : [ "PipelineActivities" ],
  "primaryIdentifier" : [ "/properties/PipelineName" ],
  "createOnlyProperties" : [ "/properties/PipelineName" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotanalytics:CreatePipeline" ]
    },
    "read" : {
      "permissions" : [ "iotanalytics:DescribePipeline", "iotanalytics:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotanalytics:UpdatePipeline", "iotanalytics:TagResource", "iotanalytics:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "iotanalytics:DeletePipeline" ]
    },
    "list" : {
      "permissions" : [ "iotanalytics:ListPipelines" ]
    }
  }
}