SCHEMA = {
  "typeName" : "AWS::Connect::ContactFlowVersion",
  "description" : "Resource Type Definition for ContactFlowVersion",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : { },
  "properties" : {
    "ContactFlowVersionARN" : {
      "description" : "The identifier of the contact flow version (ARN).",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]+:[0-9]{12}:instance/[-a-zA-Z0-9]+/contact-flow/[-a-zA-Z0-9]+:[0-9]+$",
      "minLength" : 1,
      "maxLength" : 500
    },
    "ContactFlowId" : {
      "description" : "The ARN of the contact flow this version is tied to.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]+:[0-9]{12}:instance/[-a-zA-Z0-9]+/contact-flow/[-a-zA-Z0-9]+$",
      "minLength" : 1,
      "maxLength" : 500
    },
    "Version" : {
      "description" : "The version number of this revision",
      "type" : "integer"
    },
    "Description" : {
      "description" : "The description of the version.",
      "type" : "string",
      "maxLength" : 500
    },
    "FlowContentSha256" : {
      "description" : "Indicates the checksum value of the latest published flow content",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9]{64}$",
      "minLength" : 1,
      "maxLength" : 64
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "ContactFlowId" ],
  "primaryIdentifier" : [ "/properties/ContactFlowVersionARN" ],
  "readOnlyProperties" : [ "/properties/ContactFlowVersionARN", "/properties/Version", "/properties/FlowContentSha256" ],
  "createOnlyProperties" : [ "/properties/ContactFlowId", "/properties/Description" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:CreateContactFlowVersion", "connect:DescribeContactFlow" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribeContactFlow" ]
    },
    "delete" : {
      "permissions" : [ "connect:DeleteContactFlowVersion" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ContactFlowId" : {
            "$ref" : "resource-schema.json#/properties/ContactFlowId"
          }
        },
        "required" : [ "ContactFlowId" ]
      },
      "permissions" : [ "connect:ListContactFlowVersions" ]
    },
    "update" : {
      "permissions" : [ "connect:DescribeContactFlow" ]
    }
  }
}