SCHEMA = {
  "typeName" : "AWS::Connect::ContactFlowModule",
  "description" : "Resource Type definition for AWS::Connect::ContactFlowModule.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
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
          "description" : "The value for the tag. You can specify a value that is maximum of 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
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
    "ContactFlowModuleArn" : {
      "description" : "The identifier of the contact flow module (ARN).",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/flow-module/[-a-zA-Z0-9]*$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "Name" : {
      "description" : "The name of the contact flow module.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 127,
      "pattern" : ".*\\S.*"
    },
    "Content" : {
      "description" : "The content of the contact flow module in JSON format.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256000
    },
    "Description" : {
      "description" : "The description of the contact flow module.",
      "type" : "string",
      "maxLength" : 500,
      "pattern" : ".*\\S.*"
    },
    "State" : {
      "type" : "string",
      "description" : "The state of the contact flow module.",
      "maxLength" : 500
    },
    "Status" : {
      "type" : "string",
      "description" : "The status of the contact flow module.",
      "maxLength" : 500
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
  "required" : [ "InstanceArn", "Name", "Content" ],
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
      "permissions" : [ "connect:CreateContactFlowModule", "connect:TagResource" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribeContactFlowModule" ]
    },
    "delete" : {
      "permissions" : [ "connect:DeleteContactFlowModule", "connect:UntagResource" ]
    },
    "update" : {
      "permissions" : [ "connect:UpdateContactFlowModuleMetadata", "connect:UpdateContactFlowModuleContent", "connect:TagResource", "connect:UntagResource" ]
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
      "permissions" : [ "connect:ListContactFlowModules" ]
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/ContactFlowModuleArn" ],
  "readOnlyProperties" : [ "/properties/ContactFlowModuleArn", "/properties/Status" ]
}