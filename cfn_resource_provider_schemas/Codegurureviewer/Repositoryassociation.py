SCHEMA = {
  "typeName" : "AWS::CodeGuruReviewer::RepositoryAssociation",
  "description" : "This resource schema represents the RepositoryAssociation resource in the Amazon CodeGuru Reviewer service.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-codegurureviewer",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. The allowed characters across services are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.",
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Name of the repository to be associated.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100,
      "pattern" : "^\\S[\\w.-]*$"
    },
    "Type" : {
      "description" : "The type of repository to be associated.",
      "type" : "string",
      "enum" : [ "CodeCommit", "Bitbucket", "GitHubEnterpriseServer", "S3Bucket" ]
    },
    "Owner" : {
      "description" : "The owner of the repository. For a Bitbucket repository, this is the username for the account that owns the repository.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100,
      "pattern" : "^\\S(.*\\S)?$"
    },
    "BucketName" : {
      "description" : "The name of the S3 bucket associated with an associated S3 repository. It must start with `codeguru-reviewer-`.",
      "type" : "string",
      "minLength" : 3,
      "maxLength" : 63,
      "pattern" : "^\\S(.*\\S)?$"
    },
    "ConnectionArn" : {
      "description" : "The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 256,
      "pattern" : "arn:aws(-[\\w]+)*:.+:.+:[0-9]{12}:.+"
    },
    "AssociationArn" : {
      "description" : "The Amazon Resource Name (ARN) of the repository association.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 256,
      "pattern" : "arn:aws(-[\\w]+)*:.+:.+:[0-9]{12}:.+"
    },
    "Tags" : {
      "description" : "The tags associated with a repository association.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 50,
      "uniqueItems" : False
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "Type" ],
  "readOnlyProperties" : [ "/properties/AssociationArn" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Type", "/properties/Tags", "/properties/BucketName", "/properties/Owner", "/properties/ConnectionArn" ],
  "primaryIdentifier" : [ "/properties/AssociationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "codeguru-reviewer:DescribeRepositoryAssociation", "codeguru-reviewer:AssociateRepository", "codeguru-reviewer:TagResource", "iam:CreateServiceLinkedRole", "codecommit:TagResource", "codecommit:GitPull", "codecommit:TagResource", "events:PutRule", "events:PutTargets", "codestar-connections:ListBranches", "codestar-connections:ListRepositories", "codestar-connections:ListTagsForResource", "codestar-connections:PassConnection", "codestar-connections:TagResource", "codestar-connections:UseConnection", "s3:ListBucket" ]
    },
    "read" : {
      "permissions" : [ "codeguru-reviewer:DescribeRepositoryAssociation", "codeguru-reviewer:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "codeguru-reviewer:DescribeRepositoryAssociation", "codeguru-reviewer:DisassociateRepository", "codecommit:UntagResource", "events:DeleteRule", "events:RemoveTargets", "codestar-connections:UntagResource", "codestar-connections:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "codeguru-reviewer:ListRepositoryAssociations" ]
    }
  }
}