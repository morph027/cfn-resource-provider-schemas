SCHEMA = {
  "typeName" : "AWS::MediaLive::Multiplex",
  "description" : "Resource schema for AWS::MediaLive::Multiplex",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-medialive.git",
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "The unique arn of the multiplex."
    },
    "AvailabilityZones" : {
      "description" : "A list of availability zones for the multiplex.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Destinations" : {
      "description" : "A list of the multiplex output destinations.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/MultiplexOutputDestination"
      }
    },
    "Id" : {
      "type" : "string",
      "description" : "The unique id of the multiplex."
    },
    "MultiplexSettings" : {
      "$ref" : "#/definitions/MultiplexSettings",
      "description" : "Configuration for a multiplex event."
    },
    "Name" : {
      "type" : "string",
      "description" : "Name of multiplex."
    },
    "PipelinesRunningCount" : {
      "type" : "integer",
      "description" : "The number of currently healthy pipelines."
    },
    "ProgramCount" : {
      "type" : "integer",
      "description" : "The number of programs in the multiplex."
    },
    "State" : {
      "type" : "string",
      "enum" : [ "CREATING", "CREATE_FAILED", "IDLE", "STARTING", "RUNNING", "RECOVERING", "STOPPING", "DELETING", "DELETED" ]
    },
    "Tags" : {
      "description" : "A collection of key-value pairs.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tags"
      }
    }
  },
  "definitions" : {
    "MultiplexOutputDestination" : {
      "description" : "Multiplex MediaConnect output destination settings.",
      "type" : "object",
      "properties" : {
        "MultiplexMediaConnectOutputDestinationSettings" : {
          "description" : "Multiplex MediaConnect output destination settings.",
          "properties" : {
            "EntitlementArn" : {
              "type" : "string",
              "description" : "The MediaConnect entitlement ARN available as a Flow source.",
              "minLength" : 1
            }
          },
          "additionalProperties" : False
        }
      },
      "additionalProperties" : False
    },
    "MultiplexSettings" : {
      "type" : "object",
      "description" : "A key-value pair to associate with a resource.",
      "properties" : {
        "MaximumVideoBufferDelayMilliseconds" : {
          "type" : "integer",
          "description" : "Maximum video buffer delay in milliseconds.",
          "minimum" : 800,
          "maximum" : 3000
        },
        "TransportStreamBitrate" : {
          "type" : "integer",
          "description" : "Transport stream bit rate.",
          "minimum" : 1000000,
          "maximum" : 100000000
        },
        "TransportStreamId" : {
          "type" : "integer",
          "description" : "Transport stream ID.",
          "minimum" : 0,
          "maximum" : 65535
        },
        "TransportStreamReservedBitrate" : {
          "type" : "integer",
          "description" : "Transport stream reserved bit rate.",
          "minimum" : 0,
          "maximum" : 100000000
        }
      },
      "required" : [ "TransportStreamBitrate", "TransportStreamId" ],
      "additionalProperties" : False
    },
    "Tags" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "medialive:CreateTags", "medialive:DeleteTags" ]
  },
  "additionalProperties" : False,
  "required" : [ "AvailabilityZones", "MultiplexSettings", "Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/PipelinesRunningCount", "/properties/ProgramCount", "/properties/State" ],
  "createOnlyProperties" : [ "/properties/AvailabilityZones" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "medialive:CreateMultiplex", "medialive:DescribeMultiplex", "medialive:CreateTags" ]
    },
    "read" : {
      "permissions" : [ "medialive:DescribeMultiplex" ]
    },
    "update" : {
      "permissions" : [ "medialive:UpdateMultiplex", "medialive:DescribeMultiplex", "medialive:CreateTags", "medialive:DeleteTags" ]
    },
    "delete" : {
      "permissions" : [ "medialive:DeleteMultiplex", "medialive:DescribeMultiplex" ]
    },
    "list" : {
      "permissions" : [ "medialive:ListMultiplexes" ]
    }
  }
}