SCHEMA = {
  "typeName" : "AWS::Proton::EnvironmentTemplate",
  "description" : "Definition of AWS::Proton::EnvironmentTemplate Resource Type",
  "definitions" : {
    "Provisioning" : {
      "type" : "string",
      "enum" : [ "CUSTOMER_MANAGED" ]
    },
    "Tag" : {
      "type" : "object",
      "description" : "<p>A description of a resource tag.</p>",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "<p>The key of the resource tag.</p>"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "description" : "<p>The value of the resource tag.</p>"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "<p>The Amazon Resource Name (ARN) of the environment template.</p>"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 500,
      "minLength" : 0,
      "description" : "<p>A description of the environment template.</p>"
    },
    "DisplayName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "description" : "<p>The environment template name as displayed in the developer interface.</p>"
    },
    "EncryptionKey" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 1,
      "pattern" : "^arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\\d{12}:([\\w+=,.@-]+[/:])*[\\w+=,.@-]+$",
      "description" : "<p>A customer provided encryption key that Proton uses to encrypt data.</p>"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$"
    },
    "Provisioning" : {
      "$ref" : "#/definitions/Provisioning"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 50,
      "minItems" : 0,
      "uniqueItems" : True,
      "description" : "<p>An optional list of metadata items that you can associate with the Proton environment template. A tag is a key-value pair.</p>\n         <p>For more information, see <a href=\"https://docs.aws.amazon.com/proton/latest/userguide/resources.html\">Proton resources and tagging</a> in the\n        <i>Proton User Guide</i>.</p>"
    }
  },
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/EncryptionKey", "/properties/Name", "/properties/Provisioning" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/Name" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "proton:CreateEnvironmentTemplate", "proton:DeleteEnvironmentTemplate", "proton:ListTagsForResource", "proton:TagResource", "proton:GetEnvironmentTemplate", "kms:CancelKeyDeletion", "kms:CreateAlias", "kms:CreateCustomKeyStore", "kms:CreateGrant", "kms:CreateKey", "kms:DeleteAlias", "kms:DeleteCustomKeyStore", "kms:DeleteImportedKeyMaterial", "kms:DescribeCustomKeyStores", "kms:DescribeKey", "kms:DisableKey", "kms:DisableKeyRotation", "kms:EnableKey", "kms:EnableKeyRotation", "kms:GenerateDataKey", "kms:GetKeyPolicy", "kms:GetKeyRotationStatus", "kms:GetParametersForImport", "kms:GetPublicKey", "kms:ListAliases", "kms:ListGrants", "kms:ListKeyPolicies", "kms:ListKeyRotations", "kms:ListKeys", "kms:ListResourceTags", "kms:ListRetirableGrants", "kms:PutKeyPolicy", "kms:RevokeGrant", "kms:ScheduleKeyDeletion", "kms:TagResource", "kms:UntagResource", "kms:UpdateAlias", "kms:UpdateCustomKeyStore", "kms:UpdateKeyDescription", "kms:UpdatePrimaryRegion" ]
    },
    "read" : {
      "permissions" : [ "proton:CreateEnvironmentTemplate", "proton:DeleteEnvironmentTemplate", "proton:ListTagsForResource", "proton:GetEnvironmentTemplate", "kms:CancelKeyDeletion", "kms:CreateAlias", "kms:CreateCustomKeyStore", "kms:CreateGrant", "kms:CreateKey", "kms:DeleteAlias", "kms:DeleteCustomKeyStore", "kms:DeleteImportedKeyMaterial", "kms:DescribeCustomKeyStores", "kms:DescribeKey", "kms:DisableKey", "kms:DisableKeyRotation", "kms:EnableKey", "kms:EnableKeyRotation", "kms:GenerateDataKey", "kms:GetKeyPolicy", "kms:GetKeyRotationStatus", "kms:GetParametersForImport", "kms:GetPublicKey", "kms:ListAliases", "kms:ListGrants", "kms:ListKeyPolicies", "kms:ListKeyRotations", "kms:ListKeys", "kms:ListResourceTags", "kms:ListRetirableGrants", "kms:PutKeyPolicy", "kms:RevokeGrant", "kms:ScheduleKeyDeletion", "kms:TagResource", "kms:UntagResource", "kms:UpdateAlias", "kms:UpdateCustomKeyStore", "kms:UpdateKeyDescription", "kms:UpdatePrimaryRegion" ]
    },
    "update" : {
      "permissions" : [ "proton:CreateEnvironmentTemplate", "proton:DeleteEnvironmentTemplate", "proton:GetEnvironmentTemplate", "proton:ListTagsForResource", "proton:TagResource", "proton:UpdateEnvironmentTemplate", "proton:UntagResource", "kms:CancelKeyDeletion", "kms:CreateAlias", "kms:CreateCustomKeyStore", "kms:CreateGrant", "kms:CreateKey", "kms:DeleteAlias", "kms:DeleteCustomKeyStore", "kms:DeleteImportedKeyMaterial", "kms:DescribeCustomKeyStores", "kms:DescribeKey", "kms:DisableKey", "kms:DisableKeyRotation", "kms:EnableKey", "kms:EnableKeyRotation", "kms:GenerateDataKey", "kms:GetKeyPolicy", "kms:GetKeyRotationStatus", "kms:GetParametersForImport", "kms:GetPublicKey", "kms:ListAliases", "kms:ListGrants", "kms:ListKeyPolicies", "kms:ListKeyRotations", "kms:ListKeys", "kms:ListResourceTags", "kms:ListRetirableGrants", "kms:PutKeyPolicy", "kms:RevokeGrant", "kms:ScheduleKeyDeletion", "kms:TagResource", "kms:UntagResource", "kms:UpdateAlias", "kms:UpdateCustomKeyStore", "kms:UpdateKeyDescription", "kms:UpdatePrimaryRegion" ]
    },
    "delete" : {
      "permissions" : [ "proton:CreateEnvironmentTemplate", "proton:DeleteEnvironmentTemplate", "proton:GetEnvironmentTemplate", "proton:ListTagsForResource", "proton:TagResource", "proton:UntagResource", "kms:CancelKeyDeletion", "kms:CreateAlias", "kms:CreateCustomKeyStore", "kms:CreateGrant", "kms:CreateKey", "kms:DeleteAlias", "kms:DeleteCustomKeyStore", "kms:DeleteImportedKeyMaterial", "kms:DescribeCustomKeyStores", "kms:DescribeKey", "kms:DisableKey", "kms:DisableKeyRotation", "kms:EnableKey", "kms:EnableKeyRotation", "kms:GenerateDataKey", "kms:GetKeyPolicy", "kms:GetKeyRotationStatus", "kms:GetParametersForImport", "kms:GetPublicKey", "kms:ListAliases", "kms:ListGrants", "kms:ListKeyPolicies", "kms:ListKeyRotations", "kms:ListKeys", "kms:ListResourceTags", "kms:ListRetirableGrants", "kms:PutKeyPolicy", "kms:RevokeGrant", "kms:ScheduleKeyDeletion", "kms:TagResource", "kms:UntagResource", "kms:UpdateAlias", "kms:UpdateCustomKeyStore", "kms:UpdateKeyDescription", "kms:UpdatePrimaryRegion" ]
    },
    "list" : {
      "permissions" : [ "proton:ListEnvironmentTemplates" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "proton:ListTagsForResource", "proton:UntagResource", "proton:TagResource" ]
  },
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-proton"
}