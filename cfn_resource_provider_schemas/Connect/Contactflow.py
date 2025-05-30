SCHEMA = {
  "typeName" : "AWS::Connect::ContactFlow",
  "description" : "Resource Type definition for AWS::Connect::ContactFlow",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. . You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "InstanceArn" : {
      "description" : "The identifier of the Amazon Connect instance (ARN).",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "ContactFlowArn" : {
      "description" : "The identifier of the contact flow (ARN).",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/contact-flow/[-a-zA-Z0-9]*$",
      "minLength" : 1,
      "maxLength" : 500
    },
    "Name" : {
      "description" : "The name of the contact flow.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 127
    },
    "Content" : {
      "description" : "The content of the contact flow in JSON format.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256000
    },
    "Description" : {
      "description" : "The description of the contact flow.",
      "type" : "string",
      "maxLength" : 500
    },
    "State" : {
      "type" : "string",
      "description" : "The state of the contact flow.",
      "enum" : [ "ACTIVE", "ARCHIVED" ]
    },
    "Type" : {
      "description" : "The type of the contact flow.",
      "type" : "string",
      "enum" : [ "CONTACT_FLOW", "CUSTOMER_QUEUE", "CUSTOMER_HOLD", "CUSTOMER_WHISPER", "AGENT_HOLD", "AGENT_WHISPER", "OUTBOUND_WHISPER", "AGENT_TRANSFER", "QUEUE_TRANSFER", "CAMPAIGN" ]
    },
    "Tags" : {
      "description" : "One or more tags.",
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "InstanceArn", "Content", "Name", "Type" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "connect:ListTagsForResource", "connect:UntagResource", "connect:TagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:CreateContactFlow", "connect:TagResource" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribeContactFlow" ]
    },
    "delete" : {
      "permissions" : [ "connect:DeleteContactFlow", "connect:UntagResource" ]
    },
    "update" : {
      "permissions" : [ "connect:UpdateContactFlowMetadata", "connect:UpdateContactFlowContent", "connect:TagResource", "connect:UntagResource" ]
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
      "permissions" : [ "connect:ListContactFlows" ]
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/ContactFlowArn" ],
  "readOnlyProperties" : [ "/properties/ContactFlowArn" ],
  "createOnlyProperties" : [ "/properties/Type" ]
}