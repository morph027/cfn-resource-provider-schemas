SCHEMA = {
  "typeName" : "AWS::EC2::SnapshotBlockPublicAccess",
  "description" : "Resource Type definition for AWS::EC2::SnapshotBlockPublicAccess",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ec2.git",
  "additionalProperties" : False,
  "properties" : {
    "State" : {
      "type" : "string",
      "description" : "The state of EBS Snapshot Block Public Access.",
      "enum" : [ "block-all-sharing", "block-new-sharing" ]
    },
    "AccountId" : {
      "type" : "string",
      "description" : "The identifier for the specified AWS account."
    }
  },
  "primaryIdentifier" : [ "/properties/AccountId" ],
  "readOnlyProperties" : [ "/properties/AccountId" ],
  "required" : [ "State" ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:EnableSnapshotBlockPublicAccess", "ec2:GetSnapshotBlockPublicAccessState" ]
    },
    "read" : {
      "permissions" : [ "ec2:GetSnapshotBlockPublicAccessState" ]
    },
    "update" : {
      "permissions" : [ "ec2:EnableSnapshotBlockPublicAccess", "ec2:GetSnapshotBlockPublicAccessState" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DisableSnapshotBlockPublicAccess", "ec2:GetSnapshotBlockPublicAccessState" ]
    },
    "list" : {
      "permissions" : [ "ec2:GetSnapshotBlockPublicAccessState" ]
    }
  }
}