SCHEMA = {
  "typeName" : "AWS::IVS::Stage",
  "description" : "Resource Definition for type AWS::IVS::Stage.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "AutoParticipantRecordingConfiguration" : {
      "description" : "Configuration object for individual participant recording, to attach to the new stage.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StorageConfigurationArn" : {
          "description" : "ARN of the StorageConfiguration resource to use for individual participant recording.",
          "type" : "string",
          "pattern" : "^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+$",
          "minLength" : 0,
          "maxLength" : 128
        },
        "MediaTypes" : {
          "description" : "Types of media to be recorded. Default: AUDIO_VIDEO.",
          "type" : "array",
          "minItems" : 0,
          "maxItems" : 1,
          "uniqueItems" : True,
          "insertionOrder" : False,
          "items" : {
            "type" : "string",
            "enum" : [ "AUDIO_VIDEO", "AUDIO_ONLY" ]
          },
          "default" : [ "AUDIO_VIDEO" ]
        }
      },
      "required" : [ "StorageConfigurationArn" ]
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "Stage ARN is automatically generated on creation and assigned as the unique identifier.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z]*:ivs:[a-z0-9-]+:[0-9]+:stage/[a-zA-Z0-9-]+$",
      "minLength" : 0,
      "maxLength" : 128
    },
    "Name" : {
      "description" : "Stage name",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 128,
      "pattern" : "^[a-zA-Z0-9-_]*$"
    },
    "AutoParticipantRecordingConfiguration" : {
      "$ref" : "#/definitions/AutoParticipantRecordingConfiguration"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "ActiveSessionId" : {
      "description" : "ID of the active session within the stage.",
      "type" : "string",
      "default" : "",
      "minLength" : 0,
      "maxLength" : 128
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ivs:TagResource", "ivs:UntagResource", "ivs:ListTagsForResource" ]
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/ActiveSessionId" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ivs:CreateStage", "ivs:GetStage", "ivs:TagResource", "ivs:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "ivs:GetStage", "ivs:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "ivs:GetStage", "ivs:UpdateStage", "ivs:TagResource", "ivs:UntagResource", "ivs:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "ivs:DeleteStage", "ivs:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "ivs:ListStages", "ivs:ListTagsForResource" ]
    }
  }
}