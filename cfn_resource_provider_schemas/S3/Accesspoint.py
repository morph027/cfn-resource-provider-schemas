SCHEMA = {
  "typeName" : "AWS::S3::AccessPoint",
  "description" : "The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-s3",
  "definitions" : {
    "VpcConfiguration" : {
      "description" : "The Virtual Private Cloud (VPC) configuration for a bucket access point.",
      "type" : "object",
      "properties" : {
        "VpcId" : {
          "description" : "If this field is specified, this access point will only allow connections from the specified VPC ID.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1024
        }
      }
    },
    "PublicAccessBlockConfiguration" : {
      "type" : "object",
      "properties" : {
        "BlockPublicAcls" : {
          "type" : "boolean",
          "description" : "Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to TRUE causes the following behavior:\n- PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.\n - PUT Object calls fail if the request includes a public ACL.\n. - PUT Bucket calls fail if the request includes a public ACL.\nEnabling this setting doesn't affect existing policies or ACLs."
        },
        "IgnorePublicAcls" : {
          "type" : "boolean",
          "description" : "Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to TRUE causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain. Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set."
        },
        "BlockPublicPolicy" : {
          "type" : "boolean",
          "description" : "Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to TRUE causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. Enabling this setting doesn't affect existing bucket policies."
        },
        "RestrictPublicBuckets" : {
          "type" : "boolean",
          "description" : "Specifies whether Amazon S3 should restrict public bucket policies for this bucket. Setting this element to TRUE restricts access to this bucket to only AWS services and authorized users within this account if the bucket has a public policy.\nEnabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked."
        }
      }
    },
    "Arn" : {
      "description" : "the Amazon Resource Name (ARN) of the specified accesspoint.",
      "type" : "string"
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.",
      "type" : "string",
      "pattern" : "^[a-z0-9]([a-z0-9\\-]*[a-z0-9])?$",
      "minLength" : 3,
      "maxLength" : 50
    },
    "Alias" : {
      "description" : "The alias of this Access Point. This alias can be used for compatibility purposes with other AWS services and third-party applications.",
      "type" : "string",
      "pattern" : "^[a-z0-9]([a-z0-9\\-]*[a-z0-9])?$",
      "minLength" : 3,
      "maxLength" : 63
    },
    "Bucket" : {
      "description" : "The name of the bucket that you want to associate this Access Point with.",
      "type" : "string",
      "minLength" : 3,
      "maxLength" : 255
    },
    "BucketAccountId" : {
      "description" : "The AWS account ID associated with the S3 bucket associated with this access point.",
      "type" : "string",
      "pattern" : "^\\d{12}$",
      "maxLength" : 64
    },
    "VpcConfiguration" : {
      "description" : "If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).",
      "$ref" : "#/definitions/VpcConfiguration"
    },
    "PublicAccessBlockConfiguration" : {
      "description" : "The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.",
      "$ref" : "#/definitions/PublicAccessBlockConfiguration"
    },
    "Policy" : {
      "description" : "The Access Point Policy you want to apply to this access point.",
      "type" : "object"
    },
    "NetworkOrigin" : {
      "description" : "Indicates whether this Access Point allows access from the public Internet. If VpcConfiguration is specified for this Access Point, then NetworkOrigin is VPC, and the Access Point doesn't allow access from the public Internet. Otherwise, NetworkOrigin is Internet, and the Access Point allows access from the public Internet, subject to the Access Point and bucket access policies.",
      "type" : "string",
      "enum" : [ "Internet", "VPC" ]
    },
    "Arn" : {
      "$ref" : "#/definitions/Arn",
      "description" : "The Amazon Resource Name (ARN) of the specified accesspoint.",
      "examples" : [ "arn:aws:s3:us-west-2:123456789012:accesspoint/test" ]
    }
  },
  "required" : [ "Bucket" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Bucket", "/properties/BucketAccountId", "/properties/VpcConfiguration" ],
  "readOnlyProperties" : [ "/properties/Alias", "/properties/NetworkOrigin", "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3:CreateAccessPoint", "s3:PutAccessPointPolicy", "s3:GetAccessPoint", "s3:PutAccessPointPublicAccessBlock" ]
    },
    "read" : {
      "permissions" : [ "s3:GetAccessPoint", "s3:GetAccessPointPolicy" ]
    },
    "update" : {
      "permissions" : [ "s3:PutAccessPointPolicy", "s3:PutAccessPointPublicAccessBlock", "s3:DeleteAccessPointPolicy", "s3:GetAccessPoint", "s3:GetAccessPointPolicy" ]
    },
    "delete" : {
      "permissions" : [ "s3:DeleteAccessPointPolicy", "s3:DeleteAccessPoint" ]
    },
    "list" : {
      "permissions" : [ "s3:ListAccessPoints" ]
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False
}