SCHEMA = {
  "typeName" : "AWS::CodeStarConnections::SyncConfiguration",
  "description" : "Schema for AWS::CodeStarConnections::SyncConfiguration resource which is used to enables an AWS resource to be synchronized from a source-provider.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-codestarconnections.git",
  "definitions" : { },
  "properties" : {
    "OwnerId" : {
      "description" : "the ID of the entity that owns the repository.",
      "type" : "string",
      "pattern" : "[a-za-z0-9_\\.-]+"
    },
    "ResourceName" : {
      "description" : "The name of the resource that is being synchronized to the repository.",
      "type" : "string",
      "pattern" : "[a-za-z0-9_\\.-]+"
    },
    "RepositoryName" : {
      "description" : "The name of the repository that is being synced to.",
      "type" : "string",
      "pattern" : "[a-za-z0-9_\\.-]+"
    },
    "ProviderType" : {
      "description" : "The name of the external provider where your third-party code repository is configured.",
      "type" : "string",
      "enum" : [ "GitHub", "Bitbucket", "GitHubEnterprise", "GitLab", "GitLabSelfManaged" ]
    },
    "Branch" : {
      "description" : "The name of the branch of the repository from which resources are to be synchronized,",
      "type" : "string"
    },
    "ConfigFile" : {
      "description" : "The source provider repository path of the sync configuration file of the respective SyncType.",
      "type" : "string"
    },
    "SyncType" : {
      "description" : "The type of resource synchronization service that is to be configured, for example, CFN_STACK_SYNC.",
      "type" : "string"
    },
    "RoleArn" : {
      "description" : "The IAM Role that allows AWS to update CloudFormation stacks based on content in the specified repository.",
      "type" : "string"
    },
    "PublishDeploymentStatus" : {
      "description" : "Whether to enable or disable publishing of deployment status to source providers.",
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "TriggerResourceUpdateOn" : {
      "description" : "When to trigger Git sync to begin the stack update.",
      "type" : "string",
      "enum" : [ "ANY_CHANGE", "FILE_CHANGE" ]
    },
    "RepositoryLinkId" : {
      "description" : "A UUID that uniquely identifies the RepositoryLink that the SyncConfig is associated with.",
      "type" : "string",
      "pattern" : "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
    }
  },
  "required" : [ "Branch", "ConfigFile", "RepositoryLinkId", "ResourceName", "SyncType", "RoleArn" ],
  "createOnlyProperties" : [ "/properties/SyncType", "/properties/ResourceName" ],
  "readOnlyProperties" : [ "/properties/ProviderType", "/properties/OwnerId", "/properties/RepositoryName" ],
  "primaryIdentifier" : [ "/properties/ResourceName", "/properties/SyncType" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "codestar-connections:CreateSyncConfiguration", "codestar-connections:PassRepository", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "codestar-connections:GetSyncConfiguration" ]
    },
    "update" : {
      "permissions" : [ "codestar-connections:UpdateSyncConfiguration", "codestar-connections:PassRepository", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "codestar-connections:DeleteSyncConfiguration", "codestar-connections:GetSyncConfiguration" ]
    },
    "list" : {
      "permissions" : [ "codestar-connections:ListSyncConfigurations", "codestar-connections:ListRepositoryLinks" ]
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False
}