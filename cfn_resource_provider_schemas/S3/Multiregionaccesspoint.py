SCHEMA = {
  "typeName" : "AWS::S3::MultiRegionAccessPoint",
  "description" : "AWS::S3::MultiRegionAccessPoint is an Amazon S3 resource type that dynamically routes S3 requests to easily satisfy geographic compliance requirements based on customer-defined routing policies.",
  "definitions" : {
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
      },
      "additionalProperties" : False
    },
    "Region" : {
      "type" : "object",
      "properties" : {
        "Bucket" : {
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 63,
          "pattern" : "^[a-z0-9][a-z0-9//.//-]*[a-z0-9]$",
          "relationshipRef" : {
            "typeName" : "AWS::S3::Bucket",
            "propertyPath" : "/properties/BucketName"
          }
        },
        "BucketAccountId" : {
          "type" : "string",
          "minLength" : 12,
          "maxLength" : 12,
          "pattern" : "^[0-9]{12}$"
        }
      },
      "required" : [ "Bucket" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "description" : "The name you want to assign to this Multi Region Access Point.",
      "type" : "string",
      "pattern" : "^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$",
      "minLength" : 3,
      "maxLength" : 50
    },
    "Alias" : {
      "description" : "The alias is a unique identifier to, and is part of the public DNS name for this Multi Region Access Point",
      "type" : "string"
    },
    "CreatedAt" : {
      "description" : "The timestamp of the when the Multi Region Access Point is created",
      "type" : "string"
    },
    "PublicAccessBlockConfiguration" : {
      "description" : "The PublicAccessBlock configuration that you want to apply to this Multi Region Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.",
      "$ref" : "#/definitions/PublicAccessBlockConfiguration"
    },
    "Regions" : {
      "description" : "The list of buckets that you want to associate this Multi Region Access Point with.",
      "type" : "array",
      "uniqueItems" : True,
      "minItems" : 1,
      "items" : {
        "description" : "The name of the bucket that represents of the region belonging to this Multi Region Access Point.",
        "$ref" : "#/definitions/Region"
      }
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "additionalProperties" : False,
  "required" : [ "Regions" ],
  "readOnlyProperties" : [ "/properties/Alias", "/properties/CreatedAt" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/PublicAccessBlockConfiguration", "/properties/Regions" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "s3:CreateMultiRegionAccessPoint", "s3:DescribeMultiRegionAccessPointOperation", "s3:GetMultiRegionAccessPoint" ]
    },
    "read" : {
      "permissions" : [ "s3:GetMultiRegionAccessPoint" ]
    },
    "delete" : {
      "permissions" : [ "s3:DeleteMultiRegionAccessPoint", "s3:DescribeMultiRegionAccessPointOperation", "s3:GetMultiRegionAccessPoint" ]
    },
    "list" : {
      "permissions" : [ "s3:ListMultiRegionAccessPoints" ]
    }
  }
}