SCHEMA = {
  "typeName" : "AWS::EC2::VolumeAttachment",
  "description" : "Attaches an Amazon EBS volume to a running instance and exposes it to the instance with the specified device name.\n Before this resource can be deleted (and therefore the volume detached), you must first unmount the volume in the instance. Failure to do so results in the volume being stuck in the busy state while it is trying to detach, which could possibly damage the file system or the data it contains.\n If an Amazon EBS volume is the root device of an instance, it cannot be detached while the instance is in the \"running\" state. To detach the root volume, stop the instance first.\n If the root volume is detached from an instance with an MKT product code, then the product codes from that volume are no longer associated with the instance.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "additionalProperties" : False,
  "definitions" : {
    "VolumeId" : {
      "description" : "The ID of the Amazon EBS volume",
      "type" : "string"
    },
    "Id" : {
      "description" : "",
      "type" : "string"
    },
    "InstanceId" : {
      "description" : "The ID of the instance to which the volume attaches",
      "type" : "string"
    },
    "Device" : {
      "description" : "The device name",
      "type" : "string"
    }
  },
  "properties" : {
    "VolumeId" : {
      "$ref" : "#/definitions/VolumeId",
      "description" : "The ID of the Amazon EBS volume. The volume and instance must be within the same Availability Zone. This value can be a reference to an [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html) resource, or it can be the volume ID of an existing Amazon EBS volume."
    },
    "InstanceId" : {
      "$ref" : "#/definitions/InstanceId",
      "description" : "The ID of the instance to which the volume attaches. This value can be a reference to an [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource, or it can be the physical ID of an existing EC2 instance."
    },
    "Device" : {
      "$ref" : "#/definitions/Device",
      "description" : "The device name (for example, ``/dev/sdh`` or ``xvdh``)."
    }
  },
  "required" : [ "VolumeId", "InstanceId" ],
  "primaryIdentifier" : [ "/properties/VolumeId", "/properties/InstanceId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "createOnlyProperties" : [ "/properties/Device", "/properties/InstanceId", "/properties/VolumeId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:AttachVolume", "ec2:DescribeVolumes" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeVolumes" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DetachVolume", "ec2:DescribeVolumes" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeVolumes" ]
    }
  }
}