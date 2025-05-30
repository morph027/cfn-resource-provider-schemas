SCHEMA = {
  "typeName" : "AWS::SupportApp::SlackWorkspaceConfiguration",
  "description" : "An AWS Support App resource that creates, updates, lists, and deletes Slack workspace configurations.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-supportapp.git",
  "tagging" : {
    "taggable" : False
  },
  "properties" : {
    "TeamId" : {
      "description" : "The team ID in Slack, which uniquely identifies a workspace.",
      "type" : "string",
      "pattern" : "^\\S+$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "VersionId" : {
      "description" : "An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.",
      "type" : "string",
      "pattern" : "^[0-9]+$",
      "minLength" : 1,
      "maxLength" : 256
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/TeamId" ],
  "required" : [ "TeamId" ],
  "createOnlyProperties" : [ "/properties/TeamId" ],
  "writeOnlyProperties" : [ "/properties/VersionId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "supportapp:RegisterSlackWorkspaceForOrganization", "supportapp:ListSlackWorkspaceConfigurations" ]
    },
    "read" : {
      "permissions" : [ "supportapp:ListSlackWorkspaceConfigurations" ]
    },
    "update" : {
      "permissions" : [ "supportapp:RegisterSlackWorkspaceForOrganization", "supportapp:ListSlackWorkspaceConfigurations" ]
    },
    "delete" : {
      "permissions" : [ "supportapp:ListSlackWorkspaceConfigurations", "supportapp:DeleteSlackWorkspaceConfiguration" ]
    },
    "list" : {
      "permissions" : [ "supportapp:ListSlackWorkspaceConfigurations" ]
    }
  }
}