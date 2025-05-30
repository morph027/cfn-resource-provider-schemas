SCHEMA = {
  "typeName" : "AWS::Connect::AgentStatus",
  "description" : "Resource Type definition for AWS::Connect::AgentStatus",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "InstanceArn" : {
      "description" : "The identifier of the Amazon Connect instance.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$"
    },
    "AgentStatusArn" : {
      "description" : "The Amazon Resource Name (ARN) of the agent status.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/agent-state/[-a-zA-Z0-9]*$"
    },
    "Description" : {
      "description" : "The description of the status.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 250
    },
    "Name" : {
      "description" : "The name of the status.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 127
    },
    "DisplayOrder" : {
      "description" : "The display order of the status.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 50
    },
    "State" : {
      "type" : "string",
      "description" : "The state of the status.",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "Type" : {
      "type" : "string",
      "description" : "The type of agent status.",
      "enum" : [ "ROUTABLE", "CUSTOM", "OFFLINE" ]
    },
    "ResetOrderNumber" : {
      "type" : "boolean",
      "description" : "A number indicating the reset order of the agent status."
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "LastModifiedRegion" : {
      "description" : "Last modified region.",
      "type" : "string",
      "pattern" : "[a-z]{2}(-[a-z]+){1,2}(-[0-9])?"
    },
    "LastModifiedTime" : {
      "description" : "Last modified time.",
      "type" : "number"
    }
  },
  "required" : [ "InstanceArn", "Name", "State" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:CreateAgentStatus", "connect:TagResource", "connect:ListAgentStatuses" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribeAgentStatus" ]
    },
    "delete" : {
      "permissions" : [ ]
    },
    "update" : {
      "permissions" : [ "connect:UpdateAgentStatus", "connect:UntagResource", "connect:TagResource" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "InstanceArn" : {
            "$ref" : "resource-schema.json#/properties/InstanceArn"
          }
        },
        "required" : [ "InstanceArn" ]
      },
      "permissions" : [ "connect:ListAgentStatuses" ]
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/AgentStatusArn" ],
  "readOnlyProperties" : [ "/properties/AgentStatusArn", "/properties/LastModifiedRegion", "/properties/LastModifiedTime" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "connect:TagResource", "connect:UntagResource" ]
  }
}