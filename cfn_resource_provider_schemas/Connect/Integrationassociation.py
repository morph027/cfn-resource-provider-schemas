SCHEMA = {
  "typeName" : "AWS::Connect::IntegrationAssociation",
  "description" : "Resource Type definition for AWS::Connect::IntegrationAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "IntegrationArn" : {
      "description" : "ARN of Integration being associated with the instance",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 140
    },
    "IntegrationType" : {
      "description" : "Specifies the integration type to be associated with the instance",
      "type" : "string",
      "enum" : [ "LEX_BOT", "LAMBDA_FUNCTION", "APPLICATION" ]
    },
    "InstanceId" : {
      "description" : "Amazon Connect instance identifier",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$",
      "minLength" : 1,
      "maxLength" : 100
    },
    "IntegrationAssociationId" : {
      "description" : "Identifier of the association with Connect Instance",
      "type" : "string",
      "pattern" : "^[a-zA-Z]{1}(?:-?[a-zA-Z0-9])*$"
    }
  },
  "properties" : {
    "IntegrationAssociationId" : {
      "$ref" : "#/definitions/IntegrationAssociationId"
    },
    "InstanceId" : {
      "$ref" : "#/definitions/InstanceId"
    },
    "IntegrationArn" : {
      "$ref" : "#/definitions/IntegrationArn"
    },
    "IntegrationType" : {
      "$ref" : "#/definitions/IntegrationType"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "InstanceId", "IntegrationType", "IntegrationArn" ],
  "readOnlyProperties" : [ "/properties/IntegrationAssociationId" ],
  "createOnlyProperties" : [ "/properties/InstanceId", "/properties/IntegrationArn", "/properties/IntegrationType" ],
  "primaryIdentifier" : [ "/properties/InstanceId", "/properties/IntegrationType", "/properties/IntegrationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:DescribeInstance", "ds:DescribeDirectories", "app-integrations:CreateEventIntegrationAssociation", "mobiletargeting:GetApp", "cases:GetDomain", "wisdom:GetAssistant", "wisdom:GetKnowledgeBase", "wisdom:TagResource", "voiceid:DescribeDomain", "events:PutTargets", "events:PutRule", "connect:AssociateBot", "connect:AssociateLambdaFunction", "connect:CreateIntegrationAssociation", "connect:ListBots", "connect:ListLambdaFunctions", "connect:ListIntegrationAssociations", "lambda:addPermission", "lex:GetBot", "lex:DescribeBotAlias", "lex:CreateResourcePolicy", "lex:UpdateResourcePolicy", "lex:CreateResourcePolicyStatement", "lambda:AddPermission", "app-integrations:GetApplication", "app-integrations:CreateApplicationAssociation", "iam:AttachRolePolicy", "iam:CreateServiceLinkedRole", "iam:GetRolePolicy", "iam:PutRolePolicy" ]
    },
    "read" : {
      "permissions" : [ "connect:ListBots", "connect:ListLambdaFunctions", "connect:ListIntegrationAssociations" ]
    },
    "update" : {
      "permissions" : [ ]
    },
    "delete" : {
      "permissions" : [ "connect:DescribeInstance", "ds:DescribeDirectories", "app-integrations:DeleteEventIntegrationAssociation", "app-integrations:DeleteApplicationAssociation", "events:ListTargetsByRule", "events:RemoveTargets", "events:DeleteRule", "connect:DisassociateBot", "connect:DisassociateLambdaFunction", "connect:DeleteIntegrationAssociation", "connect:ListBots", "connect:ListLambdaFunctions", "connect:ListIntegrationAssociations", "lex:DeleteResourcePolicy", "lex:DeleteResourcePolicyStatement", "lambda:RemovePermission", "iam:GetRolePolicy", "iam:DeleteRolePolicy", "iam:PutRolePolicy" ]
    },
    "list" : {
      "permissions" : [ "connect:ListBots", "connect:ListLambdaFunctions", "connect:ListIntegrationAssociations" ],
      "handlerSchema" : {
        "properties" : {
          "InstanceId" : {
            "$ref" : "resource-schema.json#/properties/InstanceId"
          }
        },
        "required" : [ "InstanceId" ]
      }
    }
  }
}