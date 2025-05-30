SCHEMA = {
  "typeName" : "AWS::CustomerProfiles::EventStream",
  "description" : "An Event Stream resource of Amazon Connect Customer Profiles",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-customer-profiles",
  "definitions" : {
    "Uri" : {
      "description" : "The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Status" : {
      "description" : "The status of enabling the Kinesis stream as a destination for export.",
      "type" : "string",
      "enum" : [ "HEALTHY", "UNHEALTHY" ]
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DomainName" : {
      "description" : "The unique name of the domain.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]+$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "EventStreamName" : {
      "description" : "The name of the event stream.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]+$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Uri" : {
      "$ref" : "#/definitions/Uri"
    },
    "EventStreamArn" : {
      "description" : "A unique identifier for the event stream.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Tags" : {
      "description" : "The tags used to organize, track, or control access for this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0,
      "maxItems" : 50
    },
    "CreatedAt" : {
      "description" : "The timestamp of when the export was created.",
      "type" : "string"
    },
    "State" : {
      "description" : "The operational state of destination stream for export.",
      "type" : "string",
      "enum" : [ "RUNNING", "STOPPED" ]
    },
    "DestinationDetails" : {
      "description" : "Details regarding the Kinesis stream.",
      "type" : "object",
      "properties" : {
        "Uri" : {
          "$ref" : "#/definitions/Uri"
        },
        "Status" : {
          "$ref" : "#/definitions/Status"
        }
      },
      "required" : [ "Uri", "Status" ],
      "additionalProperties" : False
    }
  },
  "additionalProperties" : False,
  "required" : [ "DomainName", "EventStreamName", "Uri" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "profile:TagResource", "profile:UntagResource", "profile:ListTagsForResource" ]
  },
  "createOnlyProperties" : [ "/properties/DomainName", "/properties/EventStreamName", "/properties/Uri" ],
  "readOnlyProperties" : [ "/properties/DestinationDetails", "/properties/CreatedAt", "/properties/State", "/properties/EventStreamArn" ],
  "primaryIdentifier" : [ "/properties/DomainName", "/properties/EventStreamName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "profile:CreateEventStream", "iam:PutRolePolicy", "kinesis:DescribeStreamSummary", "profile:TagResource" ]
    },
    "read" : {
      "permissions" : [ "profile:GetEventStream", "kinesis:DescribeStreamSummary" ]
    },
    "update" : {
      "permissions" : [ "kinesis:DescribeStreamSummary", "profile:GetEventStream", "profile:UntagResource", "profile:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "profile:DeleteEventStream", "iam:DeleteRolePolicy" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DomainName" : {
            "$ref" : "resource-schema.json#/properties/DomainName"
          }
        },
        "required" : [ "DomainName" ]
      },
      "permissions" : [ "profile:ListEventStreams" ]
    }
  }
}