SCHEMA = {
  "typeName" : "AWS::Events::EventBus",
  "description" : "Resource type definition for AWS::Events::EventBus",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-events",
  "properties" : {
    "EventSourceName" : {
      "description" : "If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.",
      "type" : "string"
    },
    "Name" : {
      "description" : "The name of the event bus.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "Any tags assigned to the event bus.",
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Description" : {
      "description" : "The description of the event bus.",
      "type" : "string"
    },
    "KmsKeyIdentifier" : {
      "description" : "Kms Key Identifier used to encrypt events at rest in the event bus.",
      "type" : "string"
    },
    "Policy" : {
      "description" : "A JSON string that describes the permission policy statement for the event bus.",
      "type" : [ "object", "string" ]
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) for the event bus.",
      "type" : "string"
    },
    "DeadLetterConfig" : {
      "description" : "Dead Letter Queue for the event bus.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Arn" : {
          "type" : "string"
        }
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "events:UntagResource", "events:TagResource", "events:ListTagsForResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "Name" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "writeOnlyProperties" : [ "/properties/EventSourceName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "events:CreateEventBus", "events:DescribeEventBus", "events:PutPermission", "events:ListTagsForResource", "events:TagResource", "kms:DescribeKey", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "read" : {
      "permissions" : [ "events:DescribeEventBus", "events:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "events:TagResource", "events:UntagResource", "events:PutPermission", "events:DescribeEventBus", "events:UpdateEventBus", "kms:DescribeKey", "kms:GenerateDataKey", "kms:Decrypt" ]
    },
    "delete" : {
      "permissions" : [ "events:DescribeEventBus", "events:UpdateEventBus", "events:ListTagsForResource", "events:UntagResource", "events:RemovePermission", "events:DeleteEventBus" ]
    },
    "list" : {
      "permissions" : [ "events:ListEventBuses", "events:ListTagsForResource" ]
    }
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  }
}