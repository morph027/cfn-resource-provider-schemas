SCHEMA = {
  "typeName" : "AWS::Connect::ApprovedOrigin",
  "description" : "Resource Type definition for AWS::Connect::ApprovedOrigin",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "Origin" : {
      "description" : "Domain name to be added to the allowlist of instance",
      "type" : "string",
      "maxLength" : 267
    },
    "InstanceId" : {
      "description" : "Amazon Connect instance identifier",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$",
      "minLength" : 1,
      "maxLength" : 100
    }
  },
  "properties" : {
    "Origin" : {
      "$ref" : "#/definitions/Origin"
    },
    "InstanceId" : {
      "$ref" : "#/definitions/InstanceId"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "Origin", "InstanceId" ],
  "createOnlyProperties" : [ "/properties/InstanceId", "/properties/Origin" ],
  "primaryIdentifier" : [ "/properties/InstanceId", "/properties/Origin" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:AssociateApprovedOrigin", "connect:ListApprovedOrigins" ]
    },
    "read" : {
      "permissions" : [ "connect:ListApprovedOrigins" ]
    },
    "update" : {
      "permissions" : [ ]
    },
    "delete" : {
      "permissions" : [ "connect:DisassociateApprovedOrigin", "connect:ListApprovedOrigins" ]
    },
    "list" : {
      "permissions" : [ "connect:ListApprovedOrigins" ]
    }
  }
}