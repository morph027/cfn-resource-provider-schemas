SCHEMA = {
  "typeName" : "AWS::VerifiedPermissions::PolicyTemplate",
  "description" : "Definition of AWS::VerifiedPermissions::PolicyTemplate Resource Type",
  "properties" : {
    "Description" : {
      "type" : "string",
      "maxLength" : 150,
      "minLength" : 0
    },
    "PolicyStoreId" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-]*$"
    },
    "PolicyTemplateId" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9-]*$"
    },
    "Statement" : {
      "type" : "string",
      "maxLength" : 10000,
      "minLength" : 1
    }
  },
  "required" : [ "Statement", "PolicyStoreId" ],
  "readOnlyProperties" : [ "/properties/PolicyTemplateId" ],
  "createOnlyProperties" : [ "/properties/PolicyStoreId" ],
  "primaryIdentifier" : [ "/properties/PolicyStoreId", "/properties/PolicyTemplateId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-avp",
  "handlers" : {
    "create" : {
      "permissions" : [ "verifiedpermissions:CreatePolicyTemplate", "verifiedpermissions:GetPolicyTemplate" ]
    },
    "read" : {
      "permissions" : [ "verifiedpermissions:GetPolicyTemplate" ]
    },
    "update" : {
      "permissions" : [ "verifiedpermissions:UpdatePolicyTemplate", "verifiedpermissions:GetPolicyTemplate" ]
    },
    "delete" : {
      "permissions" : [ "verifiedpermissions:DeletePolicyTemplate", "verifiedpermissions:GetPolicyTemplate" ]
    },
    "list" : {
      "permissions" : [ "verifiedpermissions:ListPolicyTemplates", "verifiedpermissions:GetPolicyTemplate" ],
      "handlerSchema" : {
        "properties" : {
          "PolicyStoreId" : {
            "$ref" : "resource-schema.json#/properties/PolicyStoreId"
          }
        },
        "required" : [ "PolicyStoreId" ]
      }
    }
  },
  "additionalProperties" : False
}