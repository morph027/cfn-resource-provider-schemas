SCHEMA = {
  "typeName" : "AWS::SecretsManager::ResourcePolicy",
  "description" : "Resource Type definition for AWS::SecretsManager::ResourcePolicy",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string",
      "description" : "The Arn of the secret."
    },
    "SecretId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 2048,
      "description" : "The ARN or name of the secret to attach the resource-based policy."
    },
    "ResourcePolicy" : {
      "type" : [ "string", "object" ],
      "description" : "A JSON-formatted string for an AWS resource-based policy."
    },
    "BlockPublicPolicy" : {
      "type" : "boolean",
      "description" : "Specifies whether to block resource-based policies that allow broad access to the secret."
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "ResourcePolicy", "SecretId" ],
  "createOnlyProperties" : [ "/properties/SecretId" ],
  "writeOnlyProperties" : [ "/properties/BlockPublicPolicy" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "secretsmanager:PutResourcePolicy", "secretsmanager:GetResourcePolicy" ]
    },
    "read" : {
      "permissions" : [ "secretsmanager:GetResourcePolicy" ]
    },
    "update" : {
      "permissions" : [ "secretsmanager:PutResourcePolicy", "secretsmanager:GetResourcePolicy" ]
    },
    "delete" : {
      "permissions" : [ "secretsmanager:DeleteResourcePolicy", "secretsmanager:GetResourcePolicy" ]
    },
    "list" : {
      "permissions" : [ "secretsmanager:GetResourcePolicy", "secretsmanager:ListSecrets" ]
    }
  }
}