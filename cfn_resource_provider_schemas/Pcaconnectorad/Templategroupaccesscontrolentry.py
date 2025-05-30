SCHEMA = {
  "typeName" : "AWS::PCAConnectorAD::TemplateGroupAccessControlEntry",
  "description" : "Definition of AWS::PCAConnectorAD::TemplateGroupAccessControlEntry Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-pcaconnectorad",
  "definitions" : {
    "AccessRight" : {
      "type" : "string",
      "enum" : [ "ALLOW", "DENY" ]
    },
    "AccessRights" : {
      "type" : "object",
      "properties" : {
        "Enroll" : {
          "$ref" : "#/definitions/AccessRight"
        },
        "AutoEnroll" : {
          "$ref" : "#/definitions/AccessRight"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AccessRights" : {
      "$ref" : "#/definitions/AccessRights"
    },
    "GroupDisplayName" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0,
      "pattern" : "^[\\x20-\\x7E]+$"
    },
    "GroupSecurityIdentifier" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 7,
      "pattern" : "^S-[0-9]-([0-9]+-){1,14}[0-9]+$"
    },
    "TemplateArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:[\\w-]+:pca-connector-ad:[\\w-]+:[0-9]+:connector(\\/[\\w-]+)\\/template(\\/[\\w-]+)$"
    }
  },
  "required" : [ "AccessRights", "GroupDisplayName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "writeOnlyProperties" : [ "/properties/AccessRights", "/properties/GroupDisplayName" ],
  "createOnlyProperties" : [ "/properties/GroupSecurityIdentifier", "/properties/TemplateArn" ],
  "primaryIdentifier" : [ "/properties/GroupSecurityIdentifier", "/properties/TemplateArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "pca-connector-ad:CreateTemplateGroupAccessControlEntry" ]
    },
    "read" : {
      "permissions" : [ "pca-connector-ad:GetTemplateGroupAccessControlEntry" ]
    },
    "update" : {
      "permissions" : [ "pca-connector-ad:UpdateTemplateGroupAccessControlEntry" ]
    },
    "delete" : {
      "permissions" : [ "pca-connector-ad:DeleteTemplateGroupAccessControlEntry", "pca-connector-ad:GetTemplateGroupAccessControlEntry" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TemplateArn" : {
            "$ref" : "resource-schema.json#/properties/TemplateArn"
          }
        },
        "required" : [ "TemplateArn" ]
      },
      "permissions" : [ "pca-connector-ad:ListTemplateGroupAccessControlEntries" ]
    }
  },
  "additionalProperties" : False
}