SCHEMA = {
  "typeName" : "AWS::NimbleStudio::Studio",
  "description" : "Represents a studio that contains other Nimble Studio resources",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-nimblestudio",
  "definitions" : {
    "StudioEncryptionConfiguration" : {
      "type" : "object",
      "description" : "<p>Configuration of the encryption method that is used for the studio.</p>",
      "properties" : {
        "KeyType" : {
          "$ref" : "#/definitions/StudioEncryptionConfigurationKeyType"
        },
        "KeyArn" : {
          "type" : "string",
          "minLength" : 4,
          "pattern" : "^arn:.*",
          "description" : "<p>The ARN for a KMS key that is used to encrypt studio data.</p>"
        }
      },
      "required" : [ "KeyType" ],
      "additionalProperties" : False
    },
    "StudioEncryptionConfigurationKeyType" : {
      "type" : "string",
      "description" : "<p>The type of KMS key that is used to encrypt studio data.</p>",
      "enum" : [ "AWS_OWNED_KEY", "CUSTOMER_MANAGED_KEY" ]
    },
    "Tags" : {
      "type" : "object",
      "description" : "",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AdminRoleArn" : {
      "type" : "string",
      "description" : "<p>The IAM role that Studio Admins will assume when logging in to the Nimble Studio portal.</p>"
    },
    "DisplayName" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 0,
      "description" : "<p>A friendly name for the studio.</p>"
    },
    "HomeRegion" : {
      "type" : "string",
      "maxLength" : 50,
      "minLength" : 0,
      "pattern" : "[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]",
      "description" : "<p>The Amazon Web Services Region where the studio resource is located.</p>"
    },
    "SsoClientId" : {
      "type" : "string",
      "description" : "<p>The Amazon Web Services SSO application client ID used to integrate with Amazon Web Services SSO to enable Amazon Web Services SSO users to log in to Nimble Studio portal.</p>"
    },
    "StudioEncryptionConfiguration" : {
      "$ref" : "#/definitions/StudioEncryptionConfiguration"
    },
    "StudioId" : {
      "type" : "string"
    },
    "StudioName" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 3,
      "pattern" : "^[a-z0-9]*$",
      "description" : "<p>The studio name that is used in the URL of the Nimble Studio portal when accessed by Nimble Studio users.</p>"
    },
    "StudioUrl" : {
      "type" : "string",
      "description" : "<p>The address of the web page for the studio.</p>"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    },
    "UserRoleArn" : {
      "type" : "string",
      "description" : "<p>The IAM role that Studio Users will assume when logging in to the Nimble Studio portal.</p>"
    }
  },
  "readOnlyProperties" : [ "/properties/HomeRegion", "/properties/SsoClientId", "/properties/StudioId", "/properties/StudioUrl" ],
  "createOnlyProperties" : [ "/properties/StudioName", "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/StudioId" ],
  "required" : [ "DisplayName", "UserRoleArn", "AdminRoleArn", "StudioName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "nimble:CreateStudio", "nimble:GetStudio", "nimble:TagResource", "sso:CreateManagedApplicationInstance", "kms:Encrypt", "kms:Decrypt", "kms:CreateGrant", "kms:ListGrants", "kms:GenerateDataKey" ]
    },
    "read" : {
      "permissions" : [ "nimble:GetStudio", "kms:Encrypt", "kms:Decrypt", "kms:ListGrants", "kms:GenerateDataKey" ]
    },
    "update" : {
      "permissions" : [ "iam:PassRole", "nimble:UpdateStudio", "nimble:GetStudio", "kms:Encrypt", "kms:Decrypt", "kms:CreateGrant", "kms:ListGrants", "kms:GenerateDataKey" ]
    },
    "delete" : {
      "permissions" : [ "nimble:DeleteStudio", "nimble:GetStudio", "nimble:UntagResource", "kms:Encrypt", "kms:Decrypt", "kms:ListGrants", "kms:RetireGrant", "kms:GenerateDataKey", "sso:DeleteManagedApplicationInstance", "sso:GetManagedApplicationInstance" ]
    },
    "list" : {
      "permissions" : [ "nimble:ListStudios" ]
    }
  },
  "additionalProperties" : False
}