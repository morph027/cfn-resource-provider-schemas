SCHEMA = {
  "typeName" : "AWS::IVSChat::Room",
  "description" : "Resource type definition for AWS::IVSChat::Room.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ivschat.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
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
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "MessageReviewHandler" : {
      "description" : "Configuration information for optional review of messages.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FallbackResult" : {
          "description" : "Specifies the fallback behavior if the handler does not return a valid response, encounters an error, or times out.",
          "type" : "string",
          "enum" : [ "ALLOW", "DENY" ],
          "default" : "ALLOW"
        },
        "Uri" : {
          "description" : "Identifier of the message review handler.",
          "type" : "string",
          "pattern" : "^$|^arn:aws:lambda:[a-z0-9-]+:[0-9]{12}:function:.+",
          "minLength" : 0,
          "maxLength" : 170
        }
      },
      "required" : [ ]
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "Room ARN is automatically generated on creation and assigned as the unique identifier.",
      "type" : "string",
      "pattern" : "^arn:aws:ivschat:[a-z0-9-]+:[0-9]+:room/[a-zA-Z0-9-]+$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Id" : {
      "description" : "The system-generated ID of the room.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9]+$",
      "minLength" : 12,
      "maxLength" : 12
    },
    "Name" : {
      "description" : "The name of the room. The value does not need to be unique.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9-_]*$",
      "minLength" : 0,
      "maxLength" : 128
    },
    "LoggingConfigurationIdentifiers" : {
      "description" : "Array of logging configuration identifiers attached to the room.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 50,
      "items" : {
        "type" : "string",
        "pattern" : "^arn:aws:ivschat:[a-z0-9-]+:[0-9]+:logging-configuration/[a-zA-Z0-9-]+$",
        "minLength" : 1,
        "maxLength" : 128
      }
    },
    "MaximumMessageLength" : {
      "description" : "The maximum number of characters in a single message.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 500,
      "default" : 500
    },
    "MaximumMessageRatePerSecond" : {
      "description" : "The maximum number of messages per second that can be sent to the room.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 10,
      "default" : 10
    },
    "MessageReviewHandler" : {
      "$ref" : "#/definitions/MessageReviewHandler"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ivschat:TagResource", "ivschat:ListTagsForResource", "ivschat:UntagResource" ]
  },
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ivschat:CreateRoom", "ivschat:TagResource" ]
    },
    "read" : {
      "permissions" : [ "ivschat:GetRoom", "ivschat:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "ivschat:UpdateRoom", "ivschat:TagResource", "ivschat:UntagResource", "ivschat:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "ivschat:DeleteRoom", "ivschat:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "ivschat:ListRooms", "ivschat:ListTagsForResource" ]
    }
  }
}