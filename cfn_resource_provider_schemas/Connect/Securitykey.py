SCHEMA = {
  "typeName" : "AWS::Connect::SecurityKey",
  "description" : "Resource Type definition for AWS::Connect::SecurityKey",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "Key" : {
      "description" : "A valid security key in PEM format.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "InstanceId" : {
      "description" : "Amazon Connect instance identifier",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$",
      "minLength" : 1,
      "maxLength" : 100
    },
    "AssociationId" : {
      "description" : "An associationID is automatically generated when a storage config is associated with an instance",
      "type" : "string",
      "pattern" : "^[-a-z0-9]*$",
      "minLength" : 1,
      "maxLength" : 100
    }
  },
  "properties" : {
    "Key" : {
      "$ref" : "#/definitions/Key"
    },
    "InstanceId" : {
      "$ref" : "#/definitions/InstanceId"
    },
    "AssociationId" : {
      "$ref" : "#/definitions/AssociationId"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "Key", "InstanceId" ],
  "readOnlyProperties" : [ "/properties/AssociationId" ],
  "createOnlyProperties" : [ "/properties/InstanceId", "/properties/Key" ],
  "primaryIdentifier" : [ "/properties/InstanceId", "/properties/AssociationId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:AssociateSecurityKey" ]
    },
    "read" : {
      "permissions" : [ "connect:ListSecurityKeys" ]
    },
    "update" : {
      "permissions" : [ ]
    },
    "delete" : {
      "permissions" : [ "connect:DisassociateSecurityKey" ]
    },
    "list" : {
      "permissions" : [ "connect:ListSecurityKeys" ]
    }
  }
}